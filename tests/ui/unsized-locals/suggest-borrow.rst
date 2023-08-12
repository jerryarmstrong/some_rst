tests/ui/unsized-locals/suggest-borrow.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: [u8] = vec!(1, 2, 3)[..]; //~ ERROR E0277
    let x: &[u8] = vec!(1, 2, 3)[..]; //~ ERROR E0308
    let x: [u8] = &vec!(1, 2, 3)[..]; //~ ERROR E0308
    //~^ ERROR E0277
    let x: &[u8] = &vec!(1, 2, 3)[..];
}


