shank-idl/tests/fixtures/accounts/single_file/complex_types.rs
==============================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankAccount)]
pub struct StructAccount {
    pub opt_vec_opt: Option<Vec<Option<u8>>>,
    pub vec_opt_pubkey: Vec<Option<Pubkey>>,
    pub opt_vec_custom_ty: Option<Vec<CustomType>>,
}


