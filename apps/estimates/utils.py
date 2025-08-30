from typing import List

from openai import OpenAI
from pydantic import BaseModel


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


client = OpenAI()


def estimate_farm_projection(farm_data: FarmInput) -> FarmProjection:
    """Call OpenAI to estimate farm project earnings."""

    # Call GPT with structured response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an agricultural investment assistant. Given farm "
                    "input, propose a project name, a ~100 word description "
                    "including an explanation of how the farmer can achieve "
                    "their goals and arrays of estimated revenue and cost for "
                    "the next 10 years. Respond ONLY in JSON matching the "
                    "schema."
                ),
            },
            {"role": "user", "content": farm_data.model_dump_json()},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "farm_projection",
                "schema": FarmProjection.model_json_schema(),
            },
        },
    )

    # Parse JSON into Pydantic model
    raw_output = response.choices[0].message.content
    if raw_output is None:
        raise ValueError("OpenAI returned no content")
    return FarmProjection.model_validate_json(raw_output)
