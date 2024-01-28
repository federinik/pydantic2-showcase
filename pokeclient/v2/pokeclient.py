import csv

import httpx
from pydantic import ValidationError

from models.pokemon import Pokemon

BASE_URL = 'https://pokeapi.co/api/v2'


def main() -> None:
    with open('pokemons.csv', '+wt', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'main_type', 'weight'], extrasaction='ignore')
        writer.writeheader()

        for i in range(1, 152):
            print(f'Get info for pokemon {i}')

            res = httpx.get(f'{BASE_URL}/pokemon/{i}')
            json = res.json()

            try:
                pokemon = Pokemon.model_validate(json)
            except ValidationError as vex:
                print(vex)
                continue

            writer.writerow(pokemon.model_dump())

    print('File is ready!')


if __name__ == '__main__':
    main()
