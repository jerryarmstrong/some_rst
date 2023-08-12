tests/ui/coercion/coerce-reborrow-multi-arg-fail.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test<T>(_a: T, _b: T) {}

fn main() {
    test(&mut 7, &7);
    //~^ mismatched types
}


