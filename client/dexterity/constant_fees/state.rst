client/dexterity/constant_fees/state.py
=======================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    from podite import (
    pod,
    I32,
    U64,
)


@pod
class FeeConfig:
    maker_fee_bps: I32
    taker_fee_bps: I32

@pod
class TraderFeeState:
    bump: U64


