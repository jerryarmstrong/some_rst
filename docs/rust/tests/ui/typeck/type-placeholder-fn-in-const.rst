tests/ui/typeck/type-placeholder-fn-in-const.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct MyStruct;

trait Test {
    const TEST: fn() -> _;
    //~^ ERROR: the placeholder `_` is not allowed within types on item signatures for functions [E0121]
    //~| ERROR: the placeholder `_` is not allowed within types on item signatures for constants [E0121]
}

impl Test for MyStruct {
    const TEST: fn() -> _ = 42;
    //~^ ERROR: the placeholder `_` is not allowed within types on item signatures for functions [E0121]
}

fn main() {}


