#!/usr/bin/env python3
from day02.main import load_regex, test
from collections import defaultdict, Counter


def load_foods(filename, script=__file__):
    return [(set(i.split(' ')), set(a.split(', '))) for i, a in load_regex(filename, r'^(.*) \(contains (.*)\)$', script=script)]


def get_allergens(foods):
    foods_by_allergen = defaultdict(list)
    for ingredients, allergens in foods:
        for allergen in allergens:
            foods_by_allergen[allergen].append(ingredients)

    possible = {allergen: set.intersection(*ingredients)
                for allergen, ingredients in foods_by_allergen.items()}

    actual = {}
    for _ in range(len(foods_by_allergen)):
        allergen, ingredient = next((allergen, next(iter(ingredients)))
                                    for allergen, ingredients in possible.items() if len(ingredients) == 1)
        del possible[allergen]
        for ingredients in possible.values():
            ingredients.discard(ingredient)
        actual[ingredient] = allergen
    return actual


def part1(filename):
    foods = load_foods(filename)
    allergens = get_allergens(foods)
    return sum(Counter(ingredient for ingredients, _ in foods for ingredient in ingredients
                       if ingredient not in allergens).values())


def part2(filename):
    foods = load_foods(filename)
    allergens = get_allergens(foods)
    return ','.join(sorted(allergens, key=allergens.get))


if __name__ == "__main__":
    test(5, part1('input-test-1.txt'))
    test(2211, part1('input.txt'))

    test('mxmxvkd,sqjhc,fvjkl', part2('input-test-1.txt'))
    test('vv,nlxsmb,rnbhjk,bvnkk,ttxvphb,qmkz,trmzkcfg,jpvz', part2('input.txt'))
