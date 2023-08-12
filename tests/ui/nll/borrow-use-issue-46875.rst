tests/ui/nll/borrow-use-issue-46875.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn vec() {
    let mut _x = vec!['c'];
    let _y = &_x;
    _x = Vec::new();
}

fn int() {
    let mut _x = 5;
    let _y = &_x;
    _x = 7;
}

fn main() {
    vec();
    int();
}


