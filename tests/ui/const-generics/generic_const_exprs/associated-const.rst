tests/ui/const-generics/generic_const_exprs/associated-const.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
struct Foo<T>(T);
impl<T> Foo<T> {
    const VALUE: usize = std::mem::size_of::<T>();
}

fn test<T>() {
    let _ = [0; Foo::<u8>::VALUE];
}

fn main() {}


