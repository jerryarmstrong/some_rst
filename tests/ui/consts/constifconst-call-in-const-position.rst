tests/ui/consts/constifconst-call-in-const-position.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // known-bug: #102498

#![feature(const_trait_impl, generic_const_exprs)]

#[const_trait]
pub trait Tr {
    fn a() -> usize;
}

impl Tr for () {
    fn a() -> usize {
        1
    }
}

const fn foo<T: ~const Tr>() -> [u8; T::a()] {
    [0; T::a()]
}

fn main() {
    foo::<()>();
}


