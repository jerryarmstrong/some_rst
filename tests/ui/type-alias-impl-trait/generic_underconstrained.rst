tests/ui/type-alias-impl-trait/generic_underconstrained.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

trait Trait {}
type Underconstrained<T: Trait> = impl Send;

// no `Trait` bound
fn underconstrain<T>(_: T) -> Underconstrained<T> {
    //~^ ERROR the trait bound `T: Trait`
    unimplemented!()
}


