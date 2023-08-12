tests/ui/typeck/issue-87935-unsized-box-expr.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]
// Box expression needs to be movable, and hence has to be of a Sized type.
fn main() {
    let _x: Box<[u32]> = box { loop {} };
    //~^ ERROR: the size for values of type `[u32]` cannot be known at compilation time

    // Check that a deduced size does not cause issues.
    let _y: Box<[u32]> = box [];
    let _z: Box<[u32; 0]> = box { loop {} };
}


