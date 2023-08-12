client/dexterity/codegen/noop_risk_engine/instructions/validate_account_liquidation.py
======================================================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from .instruction_tag import InstructionTag
from dataclasses import dataclass
from io import BytesIO
from podite import BYTES_CATALOG
from solana.publickey import PublicKey
from solana.transaction import (
    AccountMeta,
    TransactionInstruction,
)
from solmate.utils import to_account_meta
from typing import (
    List,
    Optional,
    Union,
)

# LOCK-END


# LOCK-BEGIN[ix_cls(validate_account_liquidation)]: DON'T MODIFY
@dataclass
class ValidateAccountLiquidationIx:
    program_id: PublicKey

    # account metas
    market_product_group: AccountMeta
    trader_risk_group: AccountMeta
    out_register_risk_info: AccountMeta
    risk_state_account_info: AccountMeta
    risk_model_configuration_acct: AccountMeta
    risk_signer: AccountMeta
    remaining_accounts: Optional[List[AccountMeta]]

    def to_instruction(self):
        keys = []
        keys.append(self.market_product_group)
        keys.append(self.trader_risk_group)
        keys.append(self.out_register_risk_info)
        keys.append(self.risk_state_account_info)
        keys.append(self.risk_model_configuration_acct)
        keys.append(self.risk_signer)
        if self.remaining_accounts is not None:
            keys.extend(self.remaining_accounts)

        buffer = BytesIO()
        buffer.write(InstructionTag.to_bytes(InstructionTag.VALIDATE_ACCOUNT_LIQUIDATION))

        return TransactionInstruction(
            keys=keys,
            program_id=self.program_id,
            data=buffer.getvalue(),
        )

# LOCK-END


# LOCK-BEGIN[ix_fn(validate_account_liquidation)]: DON'T MODIFY
def validate_account_liquidation(
    market_product_group: Union[str, PublicKey, AccountMeta],
    trader_risk_group: Union[str, PublicKey, AccountMeta],
    out_register_risk_info: Union[str, PublicKey, AccountMeta],
    risk_state_account_info: Union[str, PublicKey, AccountMeta],
    risk_model_configuration_acct: Union[str, PublicKey, AccountMeta],
    risk_signer: Union[str, PublicKey, AccountMeta],
    remaining_accounts: Optional[List[AccountMeta]] = None,
    program_id: Optional[PublicKey] = None,
):
    if program_id is None:
        program_id = PublicKey("Noop111111111111111111111111111111111111111")

    if isinstance(market_product_group, (str, PublicKey)):
        market_product_group = to_account_meta(
            market_product_group,
            is_signer=False,
            is_writable=False,
        )
    if isinstance(trader_risk_group, (str, PublicKey)):
        trader_risk_group = to_account_meta(
            trader_risk_group,
            is_signer=False,
            is_writable=False,
        )
    if isinstance(out_register_risk_info, (str, PublicKey)):
        out_register_risk_info = to_account_meta(
            out_register_risk_info,
            is_signer=False,
            is_writable=False,
        )
    if isinstance(risk_state_account_info, (str, PublicKey)):
        risk_state_account_info = to_account_meta(
            risk_state_account_info,
            is_signer=False,
            is_writable=False,
        )
    if isinstance(risk_model_configuration_acct, (str, PublicKey)):
        risk_model_configuration_acct = to_account_meta(
            risk_model_configuration_acct,
            is_signer=False,
            is_writable=False,
        )
    if isinstance(risk_signer, (str, PublicKey)):
        risk_signer = to_account_meta(
            risk_signer,
            is_signer=True,
            is_writable=False,
        )

    return ValidateAccountLiquidationIx(
        program_id=program_id,
        market_product_group=market_product_group,
        trader_risk_group=trader_risk_group,
        out_register_risk_info=out_register_risk_info,
        risk_state_account_info=risk_state_account_info,
        risk_model_configuration_acct=risk_model_configuration_acct,
        risk_signer=risk_signer,
        remaining_accounts=remaining_accounts,
    ).to_instruction()

# LOCK-END


