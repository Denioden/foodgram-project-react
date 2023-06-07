from enum import IntEnum


class Limits(IntEnum):
    # Максимальная длинна названия игридиента
    MAX_LEN_INGREDIENT_NAME = 100

    # Максимальная длинна еденицы измерения
    MAX_LEN_MEASUREMENT_UNIT = 20

    # Максимальная длинна имяни рецептв
    MAX_LEN_TAG_NAME = 200

    # Длинна цветового HEX-кода
    MAX_LEN_COLOR_HEX_CODE = 7

    # Максимальная длина слага
    MAX_LEN_SLUG = 200

    # Максимальная длинна имяни рецепта
    MAX_LEN_RECIPE_NAME = 200

    # Минимальное время приготовления рецепта в минутах
    MIN_COOKING_TIME = 1

    # Максимальная длина email (User)
    MAX_LEN_EMAIL_FIELD = 256
