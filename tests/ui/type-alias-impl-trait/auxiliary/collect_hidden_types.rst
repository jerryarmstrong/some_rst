tests/ui/type-alias-impl-trait/auxiliary/collect_hidden_types.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

// edition:2018

use std::future::Future;

pub trait Service<Request> {
    type Future: Future<Output = ()>;
    fn call(&mut self, req: Request) -> Self::Future;
}

// NOTE: the pub(crate) here is critical
pub(crate) fn new() -> () {}

pub struct A;
impl Service<()> for A {
    type Future = impl Future<Output = ()>;
    fn call(&mut self, _: ()) -> Self::Future {
        async { new() }
    }
}


