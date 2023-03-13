import requests


def parsing_heroes(all_heroes: dict, lst_names: tuple) -> dict:
    my_d = {}
    for hero in all_heroes:
        if hero['name'] in lst_names:
            my_d[hero['name']] = hero['powerstats']['intelligence']
    return my_d

url = 'https://akabab.github.io/superhero-api/api'
routes = '/all.json'


if __name__ == '__main__':
    resp = requests.get(f'{url}{routes}')
    our_heroes = ('Hulk', 'Captain America', 'Thanos')
    if resp.status_code == 200:
        parsing_ = parsing_heroes(resp.json(), our_heroes)
        hero, intelligence = max(parsing_.items(), key=lambda x: x[1])
        print(f' Самый умный {hero}, у него интеллект: {intelligence}')
    else:
        print('Something wrong with status_code')