tests/ui/rfc-2632-const-trait-impl/call.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_closures, const_trait_impl)]
#![allow(incomplete_features)]

pub const _: () = {
    assert!((const || true)());
};

fn main() {}


