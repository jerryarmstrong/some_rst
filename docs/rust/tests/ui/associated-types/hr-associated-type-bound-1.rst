tests/ui/associated-types/hr-associated-type-bound-1.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X<'a>
where
    for<'b> <Self as X<'b>>::U: Clone,
{
    type U: ?Sized;
    fn f(&self, x: &Self::U) {
        <Self::U>::clone(x);
    }
}

impl X<'_> for i32 {
    type U = str;
    //~^ ERROR the trait bound `str: Clone`
}

fn main() {
    1i32.f("abc");
}


