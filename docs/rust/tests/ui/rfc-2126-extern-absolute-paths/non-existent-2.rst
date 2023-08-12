tests/ui/rfc-2126-extern-absolute-paths/non-existent-2.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

fn main() {
    let s = ::xcrate::S;
    //~^ ERROR failed to resolve: could not find `xcrate` in the list of imported crates
}


