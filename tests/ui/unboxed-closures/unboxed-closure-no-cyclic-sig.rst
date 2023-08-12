tests/ui/unboxed-closures/unboxed-closure-no-cyclic-sig.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that unboxed closures cannot capture their own type.
//
// Also regression test for issue #21410.

fn g<F>(_: F) where F: FnOnce(Option<F>) {}

fn main() {
    g(|_| {  }); //~ ERROR closure/generator type that references itself
}


