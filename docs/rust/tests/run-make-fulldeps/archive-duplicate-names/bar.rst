tests/run-make-fulldeps/archive-duplicate-names/bar.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo;

fn main() {
    foo::baz();
}


