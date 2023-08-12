tests/ui/rfc-2093-infer-outlives/nested-regions.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
struct Foo<'a, 'b, T> { //~ ERROR rustc_outlives
    x: &'a &'b T
}

fn main() {}


