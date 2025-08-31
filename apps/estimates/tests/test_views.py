import json

import pytest

from apps.estimates.models import Inquiry
from apps.estimates.utils import FarmProjection


@pytest.mark.anyio
@pytest.mark.django_db(transaction=True)
async def test_get_renders_first_slide(async_client) -> None:
    response = await async_client.get("/estimate/")
    assert response.status_code == 200
    assert b'name="lot_size_acres"' in response.content


@pytest.mark.anyio
@pytest.mark.django_db(transaction=True)
async def test_post_creates_inquiry(async_client, monkeypatch) -> None:
    fake_projection = FarmProjection(
        name="Fake Project",
        description="desc",
        ten_year_revenue=[0] * 10,
        ten_year_cost=[0] * 10,
    )

    monkeypatch.setattr(
        "apps.estimates.views.estimate_farm_projection",
        lambda farm_input: fake_projection,
    )

    data = {
        "address": "123 Main St",
        "lot_size_acres": 2,
        "current_property": "House",
        "property_goal": "Expand",
        "investment_commitment": "100000",
        "excitement_notes": "Very excited",
    }
    response = await async_client.post(
        "/estimate/",
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert await Inquiry.objects.acount() == 1
    inquiry = await Inquiry.objects.aget()
    assert inquiry.address == "123 Main St"
    assert float(inquiry.lot_size_acres) == 2.0
    assert inquiry.current_property == "House"
    assert inquiry.property_goal == "Expand"
    assert inquiry.investment_commitment == "100000"
    assert inquiry.excitement_notes == "Very excited"
