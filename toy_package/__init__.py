# -*- coding: utf-8 -*-
import yapconf


SPEC = yapconf.YapconfSpec({
    'name': {'type': 'str'},
    'age': {'type': 'int'},
    'home': {'type': 'str'},
    'weight': {'type': 'int'},
})


def average(attribute, people):
    """Average the given attribute of people passed in."""
    result = 0.0
    for person in people:
        data = SPEC.load_config(person, 'ENVIRONMENT')
        for k, v in data.items():
            if k == attribute:
                result += v
    return result / len(people)
