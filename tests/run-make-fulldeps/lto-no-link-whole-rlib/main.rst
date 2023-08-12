tests/run-make-fulldeps/lto-no-link-whole-rlib/main.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate lib1;
extern crate lib2;

fn main() {
    assert_eq!(lib1::foo1(), 2);
    assert_eq!(lib2::foo2(), 2);
}


