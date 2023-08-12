tests/ui/specialization/default-associated-type-bound-2.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that generic predicates are also checked for default associated types.
#![feature(specialization)]
//~^ WARNING `specialization` is incomplete

trait X<T> {
    type U: PartialEq<T>;
    fn unsafe_compare(x: Option<Self::U>, y: Option<T>) {
        match (x, y) {
            (Some(a), Some(b)) => a == b,
            _ => false,
        };
    }
}

impl<B: 'static, T> X<B> for T {
    default type U = &'static B;
    //~^ ERROR can't compare `&'static B` with `B`
}

pub fn main() {
    <i32 as X<i32>>::unsafe_compare(None, None);
}


