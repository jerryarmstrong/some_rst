client/dexterity/codegen/dex/types/order_info.py
================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from dexterity.codegen.dex.types.fractional import Fractional
from dexterity.codegen.dex.types.operation_type import OperationType
from dexterity.utils.aob.state.base import Side
from podite import pod
from solmate.dtypes import Usize

# LOCK-END


# LOCK-BEGIN[class(OrderInfo)]: DON'T MODIFY
@pod
class OrderInfo:
    total_order_qty: "Fractional"
    matched_order_qty: "Fractional"
    order_side: Side
    is_combo: bool
    product_index: Usize
    operation_type: "OperationType"
    old_ask_qty_in_book: "Fractional"
    old_bid_qty_in_book: "Fractional"
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


