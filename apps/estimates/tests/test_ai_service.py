import json
from types import SimpleNamespace

import pytest

from apps.estimates.utils import FarmInput, FarmProjection, estimate_farm_projection


@pytest.mark.anyio
async def test_estimate_farm_projection(monkeypatch) -> None:
    farm_input = FarmInput(
        address="123 Main St",
        lot_size_acres=1.0,
        current_property="House",
        property_goal="Expand",
        investment_commitment="100000",
        excitement_notes="Excited",
    )

    fake_projection = {
        "name": "Test Project",
        "description": "desc",
        "ten_year_revenue": [1] * 10,
        "ten_year_cost": [2] * 10,
    }

    fake_response = SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(content=json.dumps(fake_projection))
            )
        ]
    )

    monkeypatch.setattr(
        "apps.estimates.utils.client.chat.completions.create",
        lambda *args, **kwargs: fake_response,
    )

    projection = estimate_farm_projection(farm_input)
    assert projection == FarmProjection(**fake_projection)
