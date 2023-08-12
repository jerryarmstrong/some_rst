tests/run-make-fulldeps/extern-multiple-copies2/bar.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
extern crate foo2; // foo2 first to exhibit the bug
#[macro_use]
extern crate foo1;

fn main() {
    foo2::foo2(foo1::A);
}


