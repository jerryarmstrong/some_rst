tests/ui/regions/regions-return-stack-allocated-vec.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we cannot return a stack allocated slice

fn function(x: isize) -> &'static [isize] {
    &[x] //~ ERROR cannot return reference to temporary value
}

fn main() {
    let x = function(1);
    let y = x[0];
}


