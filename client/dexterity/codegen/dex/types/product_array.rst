client/dexterity/codegen/dex/types/product_array.py
===================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from dexterity.codegen.dex.types.product import Product
from podite import (
    FixedLenArray,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(ProductArray)]: DON'T MODIFY
@pod
class ProductArray:
    array: FixedLenArray[Product, 256]
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


