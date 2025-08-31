import json
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Inquiry

try:
    from openai import AsyncOpenAI  # type: ignore[import-not-found]
except Exception:  # pragma: no cover - openai is optional for tests
    AsyncOpenAI = None


@csrf_exempt
async def estimate_wizard(request):
    """Render the multi-step estimate wizard or persist an inquiry."""
    if request.method == "GET":
        return render(request, "estimates/wizard.html")

    if request.method == "POST":
        body = request.body
        data = json.loads(body or b"{}")
        address = data.get("address", "")
        lot_size_acres = Decimal(str(data.get("lot_size_acres", 0)))

        inquiry: Inquiry = await Inquiry.objects.acreate(
            address=address,
            lot_size_acres=lot_size_acres,
            current_property=data.get("current_property", ""),
            property_goal=data.get("property_goal", ""),
            investment_commitment=data.get("investment_commitment", ""),
            excitement_notes=data.get("excitement_notes", ""),
        )

        estimate_text = ""
        if AsyncOpenAI is not None:
            client = AsyncOpenAI()
            try:
                response = await client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an assistant that creates property improvement estimates.",
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Address: {address}\n"
                                f"Lot size: {lot_size_acres} acres\n"
                                f"Current property: {data.get('current_property', '')}\n"
                                f"Property goal: {data.get('property_goal', '')}\n"
                                f"Investment commitment: {data.get('investment_commitment', '')}\n"
                                f"Excitement notes: {data.get('excitement_notes', '')}"
                            ),
                        },
                    ],
                )
                estimate_text = response.choices[0].message.content or ""
            except Exception:
                estimate_text = ""

        return JsonResponse({"id": inquiry.pk, "estimate": estimate_text})

    return JsonResponse({"detail": "Method not allowed"}, status=405)
