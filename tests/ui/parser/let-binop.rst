tests/ui/parser/let-binop.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let a: i8 *= 1; //~ ERROR can't reassign to an uninitialized variable
    let _ = a;
    let b += 1; //~ ERROR can't reassign to an uninitialized variable
    let _ = b;
    let c *= 1; //~ ERROR can't reassign to an uninitialized variable
    let _ = c;
}


