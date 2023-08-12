tests/ui/extern/extern-types-distinct-types.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern "C" {
    type A;
    type B;
}

fn foo(r: &A) -> &B {
    r //~ ERROR mismatched types
}

fn main() {}


