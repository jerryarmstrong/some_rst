tests/ui/mir/mir_const_prop_identity.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #91725.
//
// run-pass
// compile-flags: -Zmir-opt-level=4

fn main() {
    let a = true;
    let _ = &a;
    let mut b = false;
    b |= a;
    assert!(b);
}


