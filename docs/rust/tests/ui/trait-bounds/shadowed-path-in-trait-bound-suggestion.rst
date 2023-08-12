tests/ui/trait-bounds/shadowed-path-in-trait-bound-suggestion.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(non_snake_case)]
mod A {
    pub trait Trait {}
    impl Trait for i32 {}
}

mod B {
    pub struct A<H: A::Trait>(pub H); //~ ERROR cannot find trait
}

fn main() {
    let _ = B::A(42);
}


