tests/ui/impl-trait/negative-reasoning.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we cannot assume that an opaque type does *not* implement some
// other trait
#![feature(type_alias_impl_trait)]

trait OpaqueTrait {}
impl<T> OpaqueTrait for T {}
type OpaqueType = impl OpaqueTrait;
fn mk_opaque() -> OpaqueType {
    ()
}

#[derive(Debug)]
struct D<T>(T);

trait AnotherTrait {}
impl<T: std::fmt::Debug> AnotherTrait for T {}

// This is in error, because we cannot assume that `OpaqueType: !Debug`
impl AnotherTrait for D<OpaqueType> {
    //~^ ERROR conflicting implementations of trait `AnotherTrait` for type `D<OpaqueType>`
}

fn main() {}


