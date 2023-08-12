tests/ui/const-generics/foreign-item-const-parameter.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn foo<const X: usize>(); //~ ERROR foreign items may not have const parameters

    fn bar<T, const X: usize>(_: T); //~ ERROR foreign items may not have type or const parameters
}

fn main() {}


