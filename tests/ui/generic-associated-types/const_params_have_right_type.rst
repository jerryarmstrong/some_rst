tests/ui/generic-associated-types/const_params_have_right_type.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {
    type Foo<const N: u8>;
}

impl Trait for () {
    type Foo<const N: u64> = u32;
    //~^ error: type `Foo` has an incompatible generic parameter for trait
}

fn main() {}


