tests/ui/transmutability/primitives/unit.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! The unit type, `()`, should be one byte.

#![crate_type = "lib"]
#![feature(transmutability)]
#![allow(dead_code)]

mod assert {
    use std::mem::{Assume, BikeshedIntrinsicFrom};

    pub fn is_transmutable<Src, Dst, Context>()
    where
        Dst: BikeshedIntrinsicFrom<Src, Context, {
            Assume::ALIGNMENT
                .and(Assume::LIFETIMES)
                .and(Assume::SAFETY)
                .and(Assume::VALIDITY)
        }>
    {}
}

#[repr(C)]
struct Zst;

fn should_have_correct_size() {
    struct Context;
    assert::is_transmutable::<(), Zst, Context>();
    assert::is_transmutable::<Zst, (), Context>();
    assert::is_transmutable::<(), u8, Context>(); //~ ERROR cannot be safely transmuted
}


