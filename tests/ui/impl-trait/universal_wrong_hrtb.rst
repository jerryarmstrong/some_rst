tests/ui/impl-trait/universal_wrong_hrtb.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait<'a> {
    type Assoc;
}

fn test_argument_position(x: impl for<'a> Trait<'a, Assoc = impl Copy + 'a>) {}
//~^ ERROR `impl Trait` can only mention lifetimes bound at the fn or impl level

fn main() {}


