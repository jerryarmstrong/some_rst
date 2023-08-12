tests/ui/traits/issue-43784-supertrait.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Partial: Copy {
}

pub trait Complete: Partial {
}

impl<T> Partial for T where T: Complete {}
impl<T> Complete for T {} //~ ERROR the trait bound `T: Copy` is not satisfied

fn main() {}


