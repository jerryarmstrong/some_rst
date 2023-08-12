tests/ui/rfc-2093-infer-outlives/reference.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
struct Foo<'a, T> { //~ ERROR rustc_outlives
    bar: &'a T,
}

fn main() {}


