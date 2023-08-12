tests/ui/rfc-1937-termination-trait/termination-trait-impl-trait.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that an `impl Trait` that is not `impl Termination` will not work.
fn main() -> impl Copy { }
//~^ ERROR `main` has invalid return type `impl Copy`


