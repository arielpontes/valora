import pytest

from apps.estimates.models import Estimate, Inquiry


@pytest.fixture
def inquiry(db):
    return Inquiry.objects.create(
        address="123 Main St",
        lot_size_acres=1.5,
        current_property="House",
        property_goal="Expand",
        investment_commitment="100000",
        excitement_notes="Excited",
    )


def test_inquiry_and_estimate_persist(db, inquiry):
    estimate = Estimate.objects.create(
        inquiry=inquiry,
        project_name="Sample Project",
        description="Test description",
        net_cash_flow=1000,
        revenue=1500,
        cost=500,
    )

    assert Inquiry.objects.get(pk=inquiry.pk) == inquiry
    assert Estimate.objects.get(pk=estimate.pk).inquiry == inquiry
