tests/ui/numeric/const-scope.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const C: i32 = 1i8; //~ ERROR mismatched types
const D: i8 = C; //~ ERROR mismatched types

const fn foo() {
    let c: i32 = 1i8; //~ ERROR mismatched types
    let d: i8 = c; //~ ERROR mismatched types
}

fn main() {
    let c: i32 = 1i8; //~ ERROR mismatched types
    let d: i8 = c; //~ ERROR mismatched types
}


