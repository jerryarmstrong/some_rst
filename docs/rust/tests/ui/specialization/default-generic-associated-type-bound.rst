tests/ui/specialization/default-generic-associated-type-bound.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that default generics associated types are validated.

#![feature(specialization)]
//~^ WARNING `specialization` is incomplete

trait X {
    type U<'a>: PartialEq<&'a Self> where Self: 'a;
    fn unsafe_compare<'b>(x: Option<Self::U<'b>>, y: Option<&'b Self>) {
        match (x, y) {
            (Some(a), Some(b)) => a == b,
            _ => false,
        };
    }
}

impl<T: 'static> X for T {
    default type U<'a> = &'a T;
    //~^ ERROR can't compare `T` with `T`
}

struct NotComparable;

pub fn main() {
    <NotComparable as X>::unsafe_compare(None, None);
}


