import csv
import random

import httpx

BASE_URL = 'https://pokeapi.co/api/v2'


def main() -> None:
    with open('pokemons.csv', '+wt', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'main_type', 'weight'], extrasaction='ignore')
        writer.writeheader()

        for i in range(1, 152):
            print(f'Get info for pokemon {i}')

            res = httpx.get(f'{BASE_URL}/pokemon/{i}')
            json = res.json()

            if len(json['name']) > 7:
                print('Skipping pokemon with name length greater than 7')
                continue

            if len(json['types']) == 0:
                print('Pokemon has no types!')
                continue

            if json['types'][0]['type']['name'] not in ('grass', 'fire', 'water'):
                print('Pokemon type is not grass, fire nor water, skipping')
                continue

            if json['weight'] < 60:
                print('Pokemon is too light, skipping')
                continue

            pokemon = {
                'id': json['id'],
                'name': json['name'],
                'main_type': json['types'][0]['type']['name'],
                'weight': json['weight'] + random.randint(-5, 5)
            }

            writer.writerow(pokemon)

    print('File is ready!')


if __name__ == '__main__':
    main()
