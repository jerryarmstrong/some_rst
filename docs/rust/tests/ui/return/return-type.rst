tests/ui/return/return-type.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<T> {
    t: T,
}

fn foo<T>(x: T) -> S<T> {
    S { t: x }
}

fn bar() {
    foo(4 as usize)
    //~^ ERROR mismatched types
}

fn main() {}


