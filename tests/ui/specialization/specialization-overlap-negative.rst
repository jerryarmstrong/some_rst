tests/ui/specialization/specialization-overlap-negative.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]
#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

trait MyTrait {}

struct TestType<T>(::std::marker::PhantomData<T>);

unsafe impl<T: Clone> Send for TestType<T> {}
impl<T: MyTrait> !Send for TestType<T> {} //~ ERROR E0751

fn main() {}


