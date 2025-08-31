import json
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Estimate, Inquiry
from .utils import FarmInput, estimate_farm_projection


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

        inquiry = await Inquiry.objects.acreate(
            address=address,
            lot_size_acres=lot_size_acres,
            current_property=data.get("current_property", ""),
            property_goal=data.get("property_goal", ""),
            investment_commitment=data.get("investment_commitment", ""),
            excitement_notes=data.get("excitement_notes", ""),
        )

        farm_input = FarmInput(**data)
        projection = estimate_farm_projection(farm_input)

        total_revenue = sum(projection.ten_year_revenue)
        total_cost = sum(projection.ten_year_cost)
        net_cash_flow = total_revenue - total_cost

        estimate = await Estimate.objects.acreate(
            inquiry=inquiry,
            project_name=projection.name,
            description=projection.description,
            net_cash_flow=net_cash_flow,
            revenue=total_revenue,
            cost=total_cost,
            ten_year_revenue=projection.ten_year_revenue,
            ten_year_cost=projection.ten_year_cost,
        )

        return JsonResponse({"id": estimate.id, "projection": projection.model_dump()})

    return JsonResponse({"detail": "Method not allowed"}, status=405)


def home(request):
    """Render a list of saved project estimates."""
    estimates = Estimate.objects.all()
    return render(request, "home.html", {"estimates": estimates})


def estimate_detail(request, pk: int):
    """Render a previously generated estimate with its inquiry data."""
    estimate = get_object_or_404(Estimate, pk=pk)
    inquiry = estimate.inquiry
    return render(
        request,
        "estimates/detail.html",
        {"estimate": estimate, "inquiry": inquiry},
    )
