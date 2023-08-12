client/dexterity/codegen/dex/types/trader_fee_params.py
=======================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from dexterity.codegen.dex.types.fractional import Fractional
from dexterity.utils.aob.state.base import Side
from podite import pod
from solana.publickey import PublicKey

# LOCK-END


# LOCK-BEGIN[class(TraderFeeParams)]: DON'T MODIFY
@pod
class TraderFeeParams:
    side: Side
    is_aggressor: bool
    matched_quote_qty: "Fractional"
    matched_base_qty: "Fractional"
    product: PublicKey
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


