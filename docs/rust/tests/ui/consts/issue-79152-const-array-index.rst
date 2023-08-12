tests/ui/consts/issue-79152-const-array-index.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Regression test for issue #79152
//
// Tests that we can index an array in a const function

const fn foo() {
    let mut array = [[0; 1]; 1];
    array[0][0] = 1;
}

fn main() {}


