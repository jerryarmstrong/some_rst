tests/ui/issues/issue-4517.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar(int_param: usize) {}

fn main() {
    let foo: [u8; 4] = [1; 4];
    bar(foo);
    //~^ ERROR mismatched types
    //~| expected `usize`, found array `[u8; 4]`
}


