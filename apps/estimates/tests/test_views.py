import json

import pytest

from apps.estimates.models import Inquiry


@pytest.mark.django_db
def test_get_renders_first_slide(client):
    response = client.get("/estimate/")
    assert response.status_code == 200
    assert b'name="lot_size_acres"' in response.content


@pytest.mark.django_db
def test_post_creates_inquiry(client):
    data = {
        "address": "123 Main St",
        "lot_size_acres": 2,
        "current_property": "House",
        "property_goal": "Expand",
        "investment_commitment": "100000",
        "excitement_notes": "Very excited",
    }
    response = client.post(
        "/estimate/",
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert Inquiry.objects.count() == 1
    inquiry = Inquiry.objects.get()
    assert inquiry.address == "123 Main St"
    assert float(inquiry.lot_size_acres) == 2.0
    assert inquiry.current_property == "House"
    assert inquiry.property_goal == "Expand"
    assert inquiry.investment_commitment == "100000"
    assert inquiry.excitement_notes == "Very excited"
