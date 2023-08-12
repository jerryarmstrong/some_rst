tests/ui/on-unimplemented/feature-gate-on-unimplemented.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `#[rustc_on_unimplemented]` is gated by `rustc_attrs` feature gate.

#[rustc_on_unimplemented = "test error `{Self}` with `{Bar}`"]
//~^ ERROR this is an internal attribute that will never be stable
trait Foo<Bar>
{}

fn main() {}


