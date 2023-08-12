tests/ui/associated-types/hr-associated-type-bound-param-6.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X<'a, T>
where
    for<'b> T: X<'b, T>,
    for<'b> <T as X<'b, T>>::U: Clone,
{
    type U: ?Sized;
    fn f(x: &<T as X<'_, T>>::U) {
        <<T as X<'_, T>>::U>::clone(x);
    }
}

impl<S, T> X<'_, T> for (S,) {
    //~^ ERROR the trait bound `for<'b> T: X<'b, T>` is not satisfied
    type U = str;
}

pub fn main() {
    <(i32,) as X<i32>>::f("abc");
}


