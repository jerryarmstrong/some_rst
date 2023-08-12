tests/ui/associated-types/hr-associated-type-bound-object.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X<'a>
where
    for<'b> <Self as X<'b>>::U: Clone,
{
    type U: ?Sized;
}
fn f<'a, T: X<'a> + ?Sized>(x: &<T as X<'a>>::U) {
    //~^ ERROR the trait bound `for<'b> <T as X<'b>>::U: Clone` is not satisfied
    <<T as X<'_>>::U>::clone(x);
}

pub fn main() {
    f::<dyn X<'_, U = str>>("abc");
}


