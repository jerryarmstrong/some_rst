tests/ui/expr-if-panic-all.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// When all branches of an if expression result in panic, the entire if
// expression results in panic.

pub fn main() {
    let _x = if true {
        10
    } else {
        if true { panic!() } else { panic!() }
    };
}


