tests/ui/associated-types/hr-associated-type-bound-param-2.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Z<'a, T: ?Sized>
where
    T: Z<'a, u16>,
    //~^ the trait bound `str: Clone` is not satisfied
    //~| the trait bound `str: Clone` is not satisfied
    for<'b> <T as Z<'b, u16>>::W: Clone,
{
    type W: ?Sized;
    fn h(&self, x: &T::W) {
        <T::W>::clone(x);
    }
}

impl<'a> Z<'a, u16> for u16 {
    type W = str;
    //~^ ERROR the trait bound `str: Clone
}

fn main() {
    1u16.h("abc");
}


