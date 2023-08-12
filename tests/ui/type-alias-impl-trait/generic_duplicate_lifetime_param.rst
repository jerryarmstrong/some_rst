tests/ui/type-alias-impl-trait/generic_duplicate_lifetime_param.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

pub trait Captures<'a> {}

impl<'a, T: ?Sized> Captures<'a> for T {}

type Two<'a, 'b> = impl std::fmt::Debug + Captures<'a> + Captures<'b>;

fn one<'a>(t: &'a ()) -> Two<'a, 'a> {
    t
    //~^ ERROR non-defining opaque type use
}


