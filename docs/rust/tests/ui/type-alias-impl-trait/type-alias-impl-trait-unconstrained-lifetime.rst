tests/ui/type-alias-impl-trait/type-alias-impl-trait-unconstrained-lifetime.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for #74018

#![feature(type_alias_impl_trait)]

trait Trait {
    type Associated;
    fn into(self) -> Self::Associated;
}

impl<'a, I: Iterator<Item = i32>> Trait for (i32, I) {
    //~^ ERROR the lifetime parameter `'a` is not constrained
    type Associated = (i32, impl Iterator<Item = i32>);
    fn into(self) -> Self::Associated {
        (0_i32, [0_i32].iter().copied())
    }
}

fn main() {}


