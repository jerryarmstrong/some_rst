lang/src/account_meta.rs
========================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use crate::ToAccountMetas;
use solana_program::instruction::AccountMeta;

impl ToAccountMetas for AccountMeta {
    fn to_account_metas(&self, _is_signer: Option<bool>) -> Vec<AccountMeta> {
        vec![self.clone()]
    }
}


