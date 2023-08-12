tests/ui/generics/generic-type-params-forward-mention.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that we get an error and not an ICE for this problematic case.
struct Foo<T = Option<U>, U = bool>(T, U);
//~^ ERROR generic parameters with a default cannot use forward declared identifiers
fn main() {
    let x: Foo;
}


