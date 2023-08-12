tests/ui/cross-crate/auxiliary/xcrate-trait-lifetime-param.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait FromBuf<'a> {
    fn from_buf(_: &'a [u8]) -> Self;
}


