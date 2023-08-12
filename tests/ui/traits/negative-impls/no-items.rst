tests/ui/traits/negative-impls/no-items.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

trait MyTrait {
    type Foo;
}

impl !MyTrait for u32 {
    type Foo = i32; //~ ERROR negative impls cannot have any items
}

fn main() {}


