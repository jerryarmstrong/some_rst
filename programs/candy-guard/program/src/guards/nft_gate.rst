programs/candy-guard/program/src/guards/nft_gate.rs
===================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: rs

    use super::*;
use crate::{
    errors::CandyGuardError,
    state::GuardType,
    utils::{assert_is_token_account, assert_keys_equal},
};
use mpl_token_metadata::state::{Metadata, TokenMetadataAccount};

/// Guard that restricts the transaction to holders of a specified collection.
///
/// List of accounts required:
///
///   0. `[]` Token account of the NFT.
///   1. `[]` Metadata account of the NFT.
#[derive(AnchorSerialize, AnchorDeserialize, Clone, Debug)]
pub struct NftGate {
    pub required_collection: Pubkey,
}

impl Guard for NftGate {
    fn size() -> usize {
        32 // required_collection
    }

    fn mask() -> u64 {
        GuardType::as_mask(GuardType::NftGate)
    }
}

impl Condition for NftGate {
    fn validate<'info>(
        &self,
        ctx: &mut EvaluationContext,
        _guard_set: &GuardSet,
        _mint_args: &[u8],
    ) -> Result<()> {
        let index = ctx.account_cursor;
        // validates that we received all required accounts
        let nft_account = try_get_account_info(ctx.accounts.remaining, index)?;
        let nft_metadata = try_get_account_info(ctx.accounts.remaining, index + 1)?;
        ctx.account_cursor += 2;

        Self::verify_collection(
            nft_account,
            nft_metadata,
            &self.required_collection,
            ctx.accounts.minter.key,
        )
    }
}

impl NftGate {
    pub fn verify_collection(
        nft_account: &AccountInfo,
        nft_metadata: &AccountInfo,
        collection: &Pubkey,
        owner: &Pubkey,
    ) -> Result<()> {
        let metadata: Metadata = Metadata::from_account_info(nft_metadata)?;
        // validates the metadata information
        assert_keys_equal(nft_metadata.owner, &mpl_token_metadata::id())?;

        match metadata.collection {
            Some(c) if c.verified && c.key == *collection => Ok(()),
            _ => Err(CandyGuardError::InvalidNftCollection),
        }?;

        let account = assert_is_token_account(nft_account, owner, &metadata.mint)?;

        if account.amount < 1 {
            return err!(CandyGuardError::MissingNft);
        }

        Ok(())
    }
}


