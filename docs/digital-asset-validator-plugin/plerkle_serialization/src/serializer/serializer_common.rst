plerkle_serialization/src/serializer/serializer_common.rs
=========================================================

Last edited: 2023-08-03 21:06:53

Contents:

.. code-block:: rs

    use crate::Pubkey;

impl From<&[u8]> for Pubkey {
    fn from(slice: &[u8]) -> Self {
        let arr = <[u8; 32]>::try_from(slice);
        Pubkey::new(&arr.unwrap())
    }
}


