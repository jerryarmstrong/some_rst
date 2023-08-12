tests/run-make-fulldeps/extern-multiple-copies/bar.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo2; // foo2 first to exhibit the bug
extern crate foo1;

fn main() {
    /* ... */
}


