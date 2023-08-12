tests/ui/coherence/coherence-overlap-downstream-inherent.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we consider `T: Sugar + Fruit` to be ambiguous, even
// though no impls are found.

struct Sweet<X>(X);
pub trait Sugar {}
pub trait Fruit {}
impl<T:Sugar> Sweet<T> { fn dummy(&self) { } }
//~^ ERROR E0592
impl<T:Fruit> Sweet<T> { fn dummy(&self) { } }

trait Bar<X> {}
struct A<T, X>(T, X);
impl<X, T> A<T, X> where T: Bar<X> { fn f(&self) {} }
//~^ ERROR E0592
impl<X> A<i32, X> { fn f(&self) {} }

fn main() {}


