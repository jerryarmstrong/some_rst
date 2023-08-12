tests/ui/mir/mir_static_subtype.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that subtyping the body of a static doesn't cause an ICE.

fn foo(_ : &()) {}
static X: fn(&'static ()) = foo;

fn main() {
    let _ = X;
}


