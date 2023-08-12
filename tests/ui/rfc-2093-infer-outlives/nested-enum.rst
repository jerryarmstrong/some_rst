tests/ui/rfc-2093-infer-outlives/nested-enum.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
enum Foo<'a, T> { //~ ERROR rustc_outlives

    One(Bar<'a, T>)
}

struct Bar<'b, U> {
    field2: &'b U
}

fn main() {}


