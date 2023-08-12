tests/run-make-fulldeps/issue-15460/bar.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo;
fn main() {
    unsafe { foo::foo() }
}


