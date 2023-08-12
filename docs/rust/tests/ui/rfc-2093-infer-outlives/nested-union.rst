tests/ui/rfc-2093-infer-outlives/nested-union.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_outlives]
union Foo<'a, T: Copy> { //~ ERROR rustc_outlives
    field1: Bar<'a, T>
}

// Type U needs to outlive lifetime 'b
#[derive(Clone, Copy)]
union Bar<'b, U: Copy> {
    field2: &'b U
}

fn main() {}


