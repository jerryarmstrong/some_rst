tests/ui/nll/ty-outlives/projection-where-clause-env-wrong-bound.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to establish that `<T as
// MyTrait<'a>>::Output` outlives `'b` here. We need to prove however
// that `<T as MyTrait<'a>>::Output` outlives `'a`, so we also have to
// prove that `'b: 'a`.

trait MyTrait<'a> {
    type Output;
}

fn foo1<'a, 'b, T>() -> &'a ()
where
    T: MyTrait<'a>,
    <T as MyTrait<'a>>::Output: 'b,
{
    bar::<T::Output>() //~ ERROR may not live long enough
}

fn foo2<'a, 'b, T>() -> &'a ()
where
    T: MyTrait<'a>,
    <T as MyTrait<'a>>::Output: 'b,
    'b: 'a,
{
    bar::<T::Output>() // OK
}

fn bar<'a, T>() -> &'a ()
where
    T: 'a,
{
    &()
}

fn main() {}


