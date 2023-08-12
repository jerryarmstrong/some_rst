tests/ui/nll/ty-outlives/projection-where-clause-env.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that when we have a `<T as MyTrait<'a>>::Output: 'a`
// relationship in the environment we take advantage of it.  In this
// case, that means we **don't** have to prove that `T: 'a`.
//
// Regression test for #53121.
//
// check-pass

trait MyTrait<'a> {
    type Output;
}

fn foo<'a, T>() -> &'a ()
where
    T: MyTrait<'a>,
    <T as MyTrait<'a>>::Output: 'a,
{
    bar::<T::Output>()
}

fn bar<'a, T>() -> &'a ()
where
    T: 'a,
{
    &()
}

fn main() {}


