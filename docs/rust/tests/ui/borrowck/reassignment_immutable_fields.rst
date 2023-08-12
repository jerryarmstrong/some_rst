tests/ui/borrowck/reassignment_immutable_fields.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test is currently disallowed, but we hope someday to support it.
//
// FIXME(#21232)

fn assign_both_fields_and_use() {
    let x: (u32, u32);
    x.0 = 1; //~ ERROR
    x.1 = 22;
    drop(x.0);
    drop(x.1);
}

fn assign_both_fields_the_use_var() {
    let x: (u32, u32);
    x.0 = 1; //~ ERROR
    x.1 = 22;
    drop(x);
}

fn main() { }


