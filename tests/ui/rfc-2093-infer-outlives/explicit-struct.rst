tests/ui/rfc-2093-infer-outlives/explicit-struct.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
struct Foo<'b, U> { //~ ERROR rustc_outlives
    bar: Bar<'b, U>
}

struct Bar<'a, T> where T: 'a {
    x: &'a (),
    y: T,
}

fn main() {}


