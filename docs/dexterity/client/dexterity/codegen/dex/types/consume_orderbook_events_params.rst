client/dexterity/codegen/dex/types/consume_orderbook_events_params.py
=====================================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    U64,
    pod,
)

# LOCK-END


# LOCK-BEGIN[class(ConsumeOrderbookEventsParams)]: DON'T MODIFY
@pod
class ConsumeOrderbookEventsParams:
    max_iterations: U64
    # LOCK-END

    @classmethod
    def to_bytes(cls, obj, **kwargs):
        return cls.pack(obj, converter="bytes", **kwargs)

    @classmethod
    def from_bytes(cls, raw, **kwargs):
        return cls.unpack(raw, converter="bytes", **kwargs)


