tests/ui/rfc-2093-infer-outlives/self-structs.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
struct Foo<'a, 'b, T> { //~ ERROR rustc_outlives
    field1: dyn Bar<'a, 'b, T>
}

trait Bar<'x, 's, U>
    where U: 'x,
    Self:'s
{}

fn main() {}


