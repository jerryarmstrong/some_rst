tests/ui/traits/ignore-err-impls.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct S;

trait Generic<T> {}

impl<'a, T> Generic<&'a T> for S {}
impl Generic<Type> for S {}
//~^ ERROR cannot find type `Type` in this scope

fn main() {}


