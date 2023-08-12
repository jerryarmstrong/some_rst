tests/ui/feature-gates/feature-gate-inherent_associated_types.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that inherent associated types cannot be used when inherent_associated_types
// feature gate is not used.

struct Foo;

impl Foo {
    type Bar = isize; //~ERROR inherent associated types are unstable
}

fn main() {}


