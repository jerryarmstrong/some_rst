tests/ui/const-generics/auxiliary/const_generic_lib.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Struct<const N: usize>(pub [u8; N]);

pub type Alias = Struct<2>;

pub fn function(value: Struct<3>) -> u8 {
    value.0[0]
}


