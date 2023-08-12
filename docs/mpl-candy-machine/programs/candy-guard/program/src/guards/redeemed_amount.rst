programs/candy-guard/program/src/guards/redeemed_amount.rs
==========================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: rs

    use crate::state::GuardType;

use super::*;

/// Guard that stop the mint once the specified amount of items
/// redeenmed is reached.
#[derive(AnchorSerialize, AnchorDeserialize, Clone, Debug)]
pub struct RedeemedAmount {
    pub maximum: u64,
}

impl Guard for RedeemedAmount {
    fn size() -> usize {
        8 // maximum
    }

    fn mask() -> u64 {
        GuardType::as_mask(GuardType::RedeemedAmount)
    }
}

impl Condition for RedeemedAmount {
    fn validate<'info>(
        &self,
        ctx: &mut EvaluationContext,
        _guard_set: &GuardSet,
        _mint_args: &[u8],
    ) -> Result<()> {
        let candy_machine = &ctx.accounts.candy_machine;

        if candy_machine.items_redeemed >= self.maximum {
            return err!(CandyGuardError::MaximumRedeemedAmount);
        }

        Ok(())
    }
}


