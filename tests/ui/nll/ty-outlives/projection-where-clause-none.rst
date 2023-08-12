tests/ui/nll/ty-outlives/projection-where-clause-none.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are NOT able to establish that `<T as
// MyTrait<'a>>::Output: 'a` outlives `'a` here -- we have only one
// recourse, which is to prove that `T: 'a` and `'a: 'a`, but we don't
// know that `T: 'a`.

trait MyTrait<'a> {
    type Output;
}

fn foo<'a, T>() -> &'a ()
where
    T: MyTrait<'a>,
{
    bar::<T::Output>() //~ ERROR the parameter type `T` may not live long enough
}

fn bar<'a, T>() -> &'a ()
where
    T: 'a,
{
    &()
}

fn main() {}


