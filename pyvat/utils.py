from decimal import Decimal

from pyvat.countries import ISO_CC_TO_EC_CC


def ensure_decimal(value):
    return value if isinstance(value, Decimal) else Decimal(value)


def translate_countrycode(iso_cc, translation_table = ISO_CC_TO_EC_CC):
    """Uses translation_table to convert country-codes. Translates from ISO country codes to country codes used by the
    European Commission.
    """

    # If translation exists
    if iso_cc in translation_table:
        return translation_table[iso_cc]

    return iso_cc
