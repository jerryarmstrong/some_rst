tests/ui/generator/issue-64620-yield-array-element.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #64620

#![feature(generators)]

pub fn crash(arr: [usize; 1]) {
    yield arr[0]; //~ ERROR: yield expression outside of generator literal
}

fn main() {}


