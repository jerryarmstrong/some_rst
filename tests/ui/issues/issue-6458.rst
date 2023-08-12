tests/ui/issues/issue-6458.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker;

pub struct TypeWithState<State>(marker::PhantomData<State>);
pub struct MyState;

pub fn foo<State>(_: TypeWithState<State>) {}

pub fn bar() {
   foo(TypeWithState(marker::PhantomData));
   //~^ ERROR type annotations needed [E0282]
}

fn main() {
}


