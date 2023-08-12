shank-idl/tests/fixtures/accounts/single_file/padding.rs
========================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankAccount)]
pub struct StructAccountWithPadding {
    count: u8,
    #[padding]
    _padding: [u8; 3],
}


