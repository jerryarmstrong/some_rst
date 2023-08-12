tests/ui/generics/generic-extern.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn foo<T>(); //~ ERROR foreign items may not have type parameters
}

fn main() {
    foo::<i32>();
}


