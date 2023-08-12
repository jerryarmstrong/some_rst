client/dexterity/codegen/dex/types/operation_type.py
====================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    AutoTagType,
    Enum,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(OperationType)]: DON'T MODIFY
@pod
class OperationType(Enum[AutoTagType]):
    NEW_ORDER = None
    CANCEL_ORDER = None
    CHECK_HEALTH = None
    POSITION_TRANSFER = None
    CONSUME_EVENTS = None
    # LOCK-END

    @classmethod
    def _to_bytes_partial(cls, buffer, obj, **kwargs):
        # to modify packing, change this method
        return super()._to_bytes_partial(buffer, obj, **kwargs)

    @classmethod
    def _from_bytes_partial(cls, buffer, **kwargs):
        # to modify unpacking, change this method
        return super()._from_bytes_partial(buffer, **kwargs)

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


