tests/ui/type-alias-impl-trait/issue-58662-simplified.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(generators, generator_trait)]
#![feature(type_alias_impl_trait)]

trait Trait {}

impl<T> Trait for T {}

type Foo<'c> = impl Trait + 'c;
fn foo<'a>(rng: &'a ()) -> Foo<'a> {
    fn helper<'b>(rng: &'b ()) -> impl 'b + Trait {
        rng
    }

    helper(rng)
}

fn main() {
}


