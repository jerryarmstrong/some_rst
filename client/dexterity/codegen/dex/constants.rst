client/dexterity/codegen/dex/constants.py
=========================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import U64
from solmate.dtypes import Usize

# LOCK-END


# LOCK-BEGIN[constants]: DON'T MODIFY
NAME_LEN: Usize = 16
MAX_OUTRIGHTS: Usize = 128
MAX_PRODUCTS: Usize = 256
HEALTH_BUFFER_LEN: Usize = 32
MAX_TRADER_POSITIONS: Usize = 16
MAX_OPEN_ORDERS_PER_POSITION: U64 = 256
MAX_OPEN_ORDERS: Usize = 1024
ANCHOR_DISCRIMINANT_LEN: Usize = 8
SENTINEL: Usize = 0
CALLBACK_INFO_LEN: U64 = 40
CALLBACK_ID_LEN: U64 = 32
MAX_COMBOS: Usize = 128
MAX_LEGS: Usize = 4
SLOTS_1_MIN: U64 = 150
SLOTS_5_MIN: U64 = 750
SLOTS_15_MIN: U64 = 2250
SLOTS_60_MIN: U64 = 9000
# LOCK-END


