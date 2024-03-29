from __future__ import annotations

import random
from typing import Annotated, Any

from pydantic import BaseModel, Field, computed_field, model_validator


class Type(BaseModel):
    name: str


class TypeWrapper(BaseModel):
    type: Type


class Pokemon(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=7)]
    type_wrappers: Annotated[list[TypeWrapper], Field(alias='types', min_length=1)]
    weight: Annotated[int, Field(gt=60)]

    def model_post_init(self, _ctxt: Any) -> None:
        self.weight += random.randint(-5, 5)

    @model_validator(mode='before')
    @classmethod
    def validate_type_before(cls, data: dict) -> dict:
        assert data['types'][0]['type']['name'] in ('grass', 'fire', 'water')

        return data

    # @model_validator(mode='after')
    # def validate_types_after(self) -> 'Pokemon':
    #     assert any(t.type.name in ('grass', 'fire', 'water') for t in self.type_wrappers)

    #     return self

    @computed_field
    @property
    def main_type(self) -> str:
        return self.type_wrappers[0].type.name
