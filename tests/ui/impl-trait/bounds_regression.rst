tests/ui/impl-trait/bounds_regression.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub trait FakeGenerator {
    type Yield;
    type Return;
}

pub trait FakeFuture {
    type Output;
}

pub fn future_from_generator<
    T: FakeGenerator<Yield = ()>
>(x: T) -> impl FakeFuture<Output = T::Return> {
    GenFuture(x)
}

struct GenFuture<T: FakeGenerator<Yield = ()>>(#[allow(unused_tuple_struct_fields)] T);

impl<T: FakeGenerator<Yield = ()>> FakeFuture for GenFuture<T> {
    type Output = T::Return;
}

fn main() {}


