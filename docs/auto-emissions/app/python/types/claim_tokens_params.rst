app/python/types/claim_tokens_params.py
=======================================

Last edited: 2023-08-01 15:01:51

Contents:

.. code-block:: py

    from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class ClaimTokensParamsJSON(typing.TypedDict):
    max_amount: int


@dataclass
class ClaimTokensParams:
    layout: typing.ClassVar = borsh.CStruct("max_amount" / borsh.U64)
    max_amount: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "ClaimTokensParams":
        return cls(max_amount=obj.max_amount)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"max_amount": self.max_amount}

    def to_json(self) -> ClaimTokensParamsJSON:
        return {"max_amount": self.max_amount}

    @classmethod
    def from_json(cls, obj: ClaimTokensParamsJSON) -> "ClaimTokensParams":
        return cls(max_amount=obj["max_amount"])


