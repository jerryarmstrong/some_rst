tests/ui/coherence/coherence-blanket-conflicts-with-specific-multidispatch.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;
use std::default::Default;

// Test that a blank impl for all T conflicts with an impl for some
// specific T, even when there are multiple type parameters involved.

trait MyTrait<T> {
    fn get(&self) -> T;
}

impl<T> MyTrait<T> for T {
    fn get(&self) -> T {
        panic!()
    }
}

#[derive(Clone)]
struct MyType {
    dummy: usize
}

impl MyTrait<MyType> for MyType {
//~^ ERROR E0119
    fn get(&self) -> usize { (*self).clone() }
}

fn main() { }


