client/dexterity/codegen/dex/types/call_back_info.py
====================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    U64,
    pod,
)
from solana.publickey import PublicKey

# LOCK-END


# LOCK-BEGIN[class(CallBackInfo)]: DON'T MODIFY
@pod
class CallBackInfo:
    user_account: PublicKey
    open_orders_idx: U64
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


