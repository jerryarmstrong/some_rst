tests/ui/consts/const-eval/const_prop_errors.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub trait Foo {
    fn foo(self) -> u32;
}

impl<T> Foo for T {
    fn foo(self) -> u32 {
        fn bar<T>() { loop {} }
        bar::<T> as u32
    }
}

fn main() {}


