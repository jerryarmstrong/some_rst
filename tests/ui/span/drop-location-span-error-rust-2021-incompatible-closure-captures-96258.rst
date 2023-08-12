tests/ui/span/drop-location-span-error-rust-2021-incompatible-closure-captures-96258.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags -Wrust-2021-incompatible-closure-captures

fn main() {}

pub(crate) struct Numberer {}

impl Numberer {
    pub(crate) async fn new(
    //~^ ERROR `async fn` is not permitted in Rust 2015
        interval: Duration,
        //~^ ERROR cannot find type `Duration` in this scope
    ) -> Numberer {
        Numberer {}
    }
}


