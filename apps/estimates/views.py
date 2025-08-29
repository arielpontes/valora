import json
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Inquiry


@csrf_exempt
async def estimate_wizard(request):
    """Render the multi-step estimate wizard or persist an inquiry."""
    if request.method == "GET":
        return render(request, "estimates/wizard.html")

    if request.method == "POST":
        body = await request.body
        data = json.loads(body or b"{}")
        address = data.get("address", "")
        lot_size_acres = Decimal(str(data.get("lot_size_acres", 0)))

        inquiry = await Inquiry.objects.acreate(
            address=address,
            lot_size_acres=lot_size_acres,
            user_context=data,
        )

        return JsonResponse({"id": inquiry.id})

    return JsonResponse({"detail": "Method not allowed"}, status=405)
