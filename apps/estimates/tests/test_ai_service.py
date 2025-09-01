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

    fake_projection = FarmProjection(
        name="Test Project",
        description="desc",
        ten_year_revenue=[1] * 10,
        ten_year_cost=[2] * 10,
    )

    fake_result = SimpleNamespace(data=fake_projection)

    async def mock_agent_run(*args, **kwargs):
        return fake_result

    monkeypatch.setattr(
        "apps.estimates.utils.agent.run",
        mock_agent_run,
    )

    projection = await estimate_farm_projection(farm_input)
    assert projection == fake_projection
