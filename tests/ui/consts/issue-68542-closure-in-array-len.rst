tests/ui/consts/issue-68542-closure-in-array-len.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #68542
// Tests that we don't ICE when a closure appears
// in the length part of an array.

struct Bug {
    a: [(); (|| { 0 })()] //~ ERROR cannot call non-const closure
}

fn main() {}


