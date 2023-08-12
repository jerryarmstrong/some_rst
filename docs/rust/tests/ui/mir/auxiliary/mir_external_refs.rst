tests/ui/mir/auxiliary/mir_external_refs.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct S(pub u8);

impl S {
    pub fn hey() -> u8 { 24 }
}

pub trait X {
    fn hoy(&self) -> u8 { 25 }
}

impl X for S {}

pub enum E {
    U(u8)
}

pub fn regular_fn() -> u8 { 12 }


