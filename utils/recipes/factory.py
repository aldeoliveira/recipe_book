from random import randint
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt-BR')


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'creation_date_time': fake.date_time(),
        'category': fake.word(),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_unit': "minutes",
        'servings_amount': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'servings',
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        },
        'preparation_steps': fake.text(1000),
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
