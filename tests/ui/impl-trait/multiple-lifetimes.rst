tests/ui/impl-trait/multiple-lifetimes.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that multiple lifetimes are allowed in impl trait types.
// build-pass (FIXME(62277): could be check-pass?)

trait X<'x>: Sized {}

impl<U> X<'_> for U {}

fn multiple_lifeteimes<'a, 'b, T: 'static>(x: &'a mut &'b T) -> impl X<'b> + 'a {
    x
}

fn main() {}


