client/dexterity/codegen/dex/types/open_orders_node.py
======================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    U128,
    pod,
)
from solmate.dtypes import Usize

# LOCK-END


# LOCK-BEGIN[class(OpenOrdersNode)]: DON'T MODIFY
@pod
class OpenOrdersNode:
    id: U128
    client_id: U128
    prev: Usize
    next: Usize
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


