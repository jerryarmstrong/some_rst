tests/ui/rfc-2093-infer-outlives/explicit-union.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
union Foo<'b, U: Copy> { //~ ERROR rustc_outlives
    bar: Bar<'b, U>
}

#[derive(Clone, Copy)]
union Bar<'a, T: Copy> where T: 'a {
    x: &'a (),
    y: T,
}

fn main() {}


