tests/ui/const-generics/broken-mir-1.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub trait Foo {
    fn foo(&self);
}


impl<T, const N: usize> Foo for [T; N] {
    fn foo(&self) {
        let _ = &self;
    }
}

fn main() {}


