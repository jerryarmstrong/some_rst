tests/ui/nll/ty-outlives/projection-where-clause-env-wrong-lifetime.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that if we need to prove that `<T as MyTrait<'a>>::Output:
// 'a`, but we only know that `<T as MyTrait<'b>>::Output: 'a`, that
// doesn't suffice.

trait MyTrait<'a> {
    type Output;
}

fn foo1<'a, 'b, T>() -> &'a ()
where
    for<'x> T: MyTrait<'x>,
    <T as MyTrait<'b>>::Output: 'a,
{
    bar::<<T as MyTrait<'a>>::Output>()
    //~^ ERROR the associated type `<T as MyTrait<'_>>::Output` may not live long enough
}

fn bar<'a, T>() -> &'a ()
where
    T: 'a,
{
    &()
}

fn main() {}


