tests/ui/borrowck/reassignment_immutable_fields_twice.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should never be allowed -- since `x` is not `mut`, so `x.0`
// cannot be assigned twice.

fn var_then_field() {
    let x: (u32, u32);
    x = (22, 44);
    x.0 = 1; //~ ERROR
}

fn same_field_twice() {
    let x: (u32, u32);
    x.0 = 1; //~ ERROR
    x.0 = 22;
    x.1 = 44;
}

fn main() { }


