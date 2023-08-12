tests/ui/borrowck/borrowck-use-uninitialized-in-cast.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we detect unused values that are cast to other things.
// The problem was specified to casting to `*`, as creating unsafe
// pointers was not being fully checked. Issue #20791.

fn main() {
    let x: &i32;
    let y = x as *const i32; //~ ERROR [E0381]
}


