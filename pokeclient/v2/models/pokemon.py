from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field, computed_field, model_validator


class Type(BaseModel):
    name: str


class TypeWrapper(BaseModel):
    type: Type


class Pokemon(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=7)]
    types: Annotated[list[TypeWrapper], Field(min_length=1)]
    weight: Annotated[int, Field(gt=60)]

    # @model_validator(mode='after')
    # def validate_types_after(self) -> 'Pokemon':
    #     assert any(t.type.name in ('grass', 'fire', 'water') for t in self.types)

    #     return self

    @model_validator(mode='before')
    @classmethod
    def validate_type_before(cls, data: dict) -> dict:
        assert data['types'][0]['type']['name'] in ('grass', 'fire', 'water')

        return data

    @computed_field
    @property
    def main_type(self) -> str:
        return self.types[0].type.name
