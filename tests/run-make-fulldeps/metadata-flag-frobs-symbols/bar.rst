tests/run-make-fulldeps/metadata-flag-frobs-symbols/bar.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo1;
extern crate foo2;

fn main() {
    let a = foo1::foo();
    let b = foo2::foo();
    assert!(a as *const _ != b as *const _);
}


