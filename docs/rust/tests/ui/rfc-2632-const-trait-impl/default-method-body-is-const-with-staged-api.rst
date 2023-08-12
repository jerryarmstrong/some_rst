tests/ui/rfc-2632-const-trait-impl/default-method-body-is-const-with-staged-api.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// This was an ICE, because the compiler ensures the
// function to be const when performing const checking,
// but functions marked with the attribute are not const
// *and* subject to const checking.

#![feature(staged_api)]
#![feature(const_trait_impl)]
#![stable(since = "1", feature = "foo")]

#[const_trait]
trait Tr {
    fn a() {}
}

fn main() {}


