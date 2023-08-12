client/dexterity/codegen/alpha_risk_engine/instructions/instruction_tag.py
==========================================================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    # LOCK-BEGIN[imports]: DON'T MODIFY
from podite import (
    Enum,
    U64,
    pod,
)
from solmate.anchor import InstructionDiscriminant

# LOCK-END


# LOCK-BEGIN[instruction_tag]: DON'T MODIFY
@pod
class InstructionTag(Enum[U64]):
    VALIDATE_ACCOUNT_HEALTH = InstructionDiscriminant()
    VALIDATE_ACCOUNT_LIQUIDATION = InstructionDiscriminant()
    CREATE_RISK_STATE_ACCOUNT = InstructionDiscriminant()
    # LOCK-END


