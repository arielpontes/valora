from typing import List

from django.conf import settings
from pydantic import BaseModel
from pydantic_ai import Agent


class FarmInput(BaseModel):
    address: str
    lot_size_acres: float
    current_property: str
    property_goal: str
    investment_commitment: str
    excitement_notes: str


class FarmProjection(BaseModel):
    name: str
    description: str
    ten_year_revenue: List[int]
    ten_year_cost: List[int]


SYSTEM_PROMPT = (
    "You are an agricultural investment assistant. Given farm "
    "input, propose a project name, a ~100 word description "
    "including an explanation of how the farmer can achieve "
    "their goals and arrays of estimated revenue and cost for "
    "the next 10 years. Respond ONLY in JSON matching the "
    "schema."
)


def create_agent(system_prompt, **kwargs) -> Agent:
    """
    Create an agent instance using the default model for basic operations like
    chat.
    """
    return Agent(
        settings.AI_DEFAULT_MODEL,
        system_prompt=system_prompt,
        retries=settings.AI_AGENT_MAX_RETRIES,
        **kwargs,
    )


agent = create_agent(system_prompt=SYSTEM_PROMPT)


async def estimate_farm_projection(farm_data: FarmInput) -> FarmProjection:
    """Call Pydantic AI to estimate farm project earnings."""
    result = await agent.run(
        farm_data.model_dump_json(), result_type=FarmProjection
    )  # pyright: ignore
    return result.data
