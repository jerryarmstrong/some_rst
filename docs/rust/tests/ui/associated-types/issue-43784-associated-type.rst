tests/ui/associated-types/issue-43784-associated-type.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Partial<X: ?Sized>: Copy {
}

pub trait Complete {
    type Assoc: Partial<Self>;
}

impl<T> Partial<T> for T::Assoc where
    T: Complete
{
}

impl<T> Complete for T {
    type Assoc = T; //~ ERROR the trait bound `T: Copy` is not satisfied
}

fn main() {}


