tests/ui/coercion/coerce-reborrow-multi-arg.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
fn test<T>(_a: T, _b: T) {}

fn main() {
    test(&7, &7);
    test(&7, &mut 7);
    test::<&i32>(&mut 7, &7);
    test::<&i32>(&mut 7, &mut 7);
}


