tests/ui/marker_trait_attr/unsound-overlap.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(marker_trait_attr)]

#[marker]
trait A {}

trait B {}

impl<T: A> B for T {}
impl<T: B> A for T {}
impl A for &str {}
impl<T: A + B> A for (T,) {}
trait TraitWithAssoc {
    type Assoc;
}

impl<T: A> TraitWithAssoc for T {
    type Assoc = T;
}

impl TraitWithAssoc for ((&str,),) {
    //~^ ERROR conflicting implementations
    type Assoc = ((&'static str,),);
}

fn main() {}


