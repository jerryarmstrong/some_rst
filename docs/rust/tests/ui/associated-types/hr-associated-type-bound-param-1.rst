tests/ui/associated-types/hr-associated-type-bound-param-1.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Y<'a, T: ?Sized>
where
    T: Y<'a, Self>,
    for<'b> <Self as Y<'b, T>>::V: Clone,
    for<'b> <T as Y<'b, Self>>::V: Clone,
{
    type V: ?Sized;
    fn g(&self, x: &Self::V) {
        <Self::V>::clone(x);
    }
}

impl<'a> Y<'a, u8> for u8 {
    type V = str;
    //~^ ERROR the trait bound `str: Clone` is not satisfied
}

fn main() {
    1u8.g("abc");
}


