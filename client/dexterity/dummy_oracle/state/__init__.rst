client/dexterity/dummy_oracle/state/__init__.py
===============================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    from .common import AccountTag

from .clock import (
    Clock,
)
from .oracle_price import (
    OraclePrice,
)


def account_parser(data):
    tag = AccountTag.from_bytes(data[:1], byteorder="little")
    if tag == AccountTag.UNINITIALIZED:
        return None
    elif tag == AccountTag.ORACLE_PRICE:
        return OraclePrice.from_bytes(data)
    raise ValueError()


__all__ = [
    "Clock",
    "AccountTag",
    "OraclePrice",
    "account_parser",
]


