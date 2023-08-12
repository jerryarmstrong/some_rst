tests/ui/return/return-impl-trait.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

trait Trait {}
impl Trait for () {}

// this works
fn foo() -> impl Trait {
    ()
}

fn bar<T: Trait + std::marker::Sync>() -> T
where
    T: Send,
{
    () //~ ERROR mismatched types
}

fn other_bounds<T>() -> T
where
    T: Trait,
    Vec<usize>: Clone,
{
    () //~ ERROR mismatched types
}

fn main() {
    foo();
    bar::<()>();
    other_bounds::<()>();
}


