tests/ui/typeck/typeck_type_placeholder_mismatch.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that genuine type errors with partial
// type hints are understandable.

use std::marker::PhantomData;

struct Foo<T>(PhantomData<T>);
struct Bar<U>(PhantomData<U>);

pub fn main() {
}

fn test1() {
    let x: Foo<_> = Bar::<usize>(PhantomData);
    //~^ ERROR mismatched types
    //~| expected struct `Foo<_>`
    //~| found struct `Bar<usize>`
    //~| expected struct `Foo`, found struct `Bar`
    let y: Foo<usize> = x;
}

fn test2() {
    let x: Foo<_> = Bar::<usize>(PhantomData);
    //~^ ERROR mismatched types
    //~| expected struct `Foo<_>`
    //~| found struct `Bar<usize>`
    //~| expected struct `Foo`, found struct `Bar`
}


