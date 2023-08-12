tests/ui/packed/auxiliary/packed.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(packed)]
pub struct P1S5 {
    a: u8,
    b: u32
}

#[repr(packed(2))]
pub struct P2S6 {
    a: u8,
    b: u32,
    c: u8
}

#[repr(C, packed(2))]
pub struct P2CS8 {
    a: u8,
    b: u32,
    c: u8
}


