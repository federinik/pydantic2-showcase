from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, TypeAdapter


class Presenter(BaseModel):
    name: str
    job: str
    techs: list
    years_of_python: float
    favorite_ide: str
    dark_mode: bool


fede = Presenter(
    name='Federico Tomasi',
    job='software developer',
    techs=[
        'c#',
        'python',
        'backend',
        'docker',
        'kubernetes',
        'API'
    ],
    years_of_python=2.5,
    favorite_ide='VSCode',
    dark_mode=True
)


@dataclass
class Vanilla:
    name: str
    age: int
    job: str

    def __repr__(self) -> str:
        return f'{self.name}, {self.age}, {self.job}'


VanillaType = TypeAdapter(Vanilla)

print(repr(VanillaType.validate_python(Vanilla('John', 42, 'megadirettoregalattico'))))
print(repr(VanillaType.validate_python(Vanilla('John', None, 79))))
