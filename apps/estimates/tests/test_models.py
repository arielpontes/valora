import pytest
from asgiref.sync import sync_to_async

from apps.estimates.models import Estimate, Inquiry


@pytest.mark.anyio
@pytest.mark.django_db(transaction=True)
async def test_inquiry_and_estimate_persist() -> None:
    """Ensure Inquiry and Estimate are saved and related asynchronously."""
    inquiry = await sync_to_async(Inquiry.objects.create)(
        address="123 Main St",
        lot_size_acres=1.5,
        current_property="House",
        property_goal="Expand",
        investment_commitment="100000",
        excitement_notes="Excited",
    )

    estimate = await sync_to_async(Estimate.objects.create)(
        inquiry=inquiry,
        project_name="Sample Project",
        description="Test description",
        net_cash_flow=1000,
        revenue=1500,
        cost=500,
    )

    assert await sync_to_async(Inquiry.objects.get)(pk=inquiry.pk) == inquiry
    fetched_estimate = await sync_to_async(Estimate.objects.get)(pk=estimate.pk)
    assert fetched_estimate.inquiry == inquiry
