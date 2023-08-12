tests/ui/nll/capture-mut-ref.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

// Check that capturing a mutable reference by move and assigning to its
// referent doesn't make the unused mut lint think that it is mutable.

#![deny(unused_mut)]

pub fn mutable_upvar() {
    let mut x = &mut 0;
    //~^ ERROR
    let _ = move || {
        *x = 1;
    };
}

fn main() {}


