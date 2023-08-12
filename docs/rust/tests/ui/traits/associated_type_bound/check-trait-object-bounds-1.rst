tests/ui/traits/associated_type_bound/check-trait-object-bounds-1.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we validate associated type bounds for trait objects

trait X {
    type Y: Clone;
}

fn f<T: X + ?Sized>() {
    None::<T::Y>.clone();
}

fn main() {
    f::<dyn X<Y = str>>();
    //~^ ERROR the trait bound `str: Clone` is not satisfied
}


