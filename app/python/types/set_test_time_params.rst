app/python/types/set_test_time_params.py
========================================

Last edited: 2023-08-01 15:01:51

Contents:

.. code-block:: py

    from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SetTestTimeParamsJSON(typing.TypedDict):
    time: int


@dataclass
class SetTestTimeParams:
    layout: typing.ClassVar = borsh.CStruct("time" / borsh.U64)
    time: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SetTestTimeParams":
        return cls(time=obj.time)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"time": self.time}

    def to_json(self) -> SetTestTimeParamsJSON:
        return {"time": self.time}

    @classmethod
    def from_json(cls, obj: SetTestTimeParamsJSON) -> "SetTestTimeParams":
        return cls(time=obj["time"])


