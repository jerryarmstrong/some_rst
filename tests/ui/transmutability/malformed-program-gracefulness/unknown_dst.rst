tests/ui/transmutability/malformed-program-gracefulness/unknown_dst.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // An unknown destination type should be gracefully handled.

#![crate_type = "lib"]
#![feature(transmutability)]
#![allow(dead_code, incomplete_features, non_camel_case_types)]

mod assert {
    use std::mem::BikeshedIntrinsicFrom;
    pub struct Context;

    pub fn is_transmutable<Src, Dst, Context>()
    where
        Dst: BikeshedIntrinsicFrom<Src, Context>
    {}
}

fn should_gracefully_handle_unknown_dst() {
    struct Context;
    struct Src;
    assert::is_transmutable::<Src, Dst, Context>(); //~ cannot find type
}


