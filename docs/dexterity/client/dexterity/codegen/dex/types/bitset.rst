client/dexterity/codegen/dex/types/bitset.py
============================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    FixedLenArray,
    U128,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(Bitset)]: DON'T MODIFY
@pod
class Bitset:
    inner: FixedLenArray[U128, 2]
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


