tests/ui/nll/ty-outlives/projection-body.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that when we infer the lifetime to a subset of the fn body, it
// works out.
//
// check-pass

trait MyTrait<'a> {
    type Output;
}

fn foo1<T>()
where
    for<'x> T: MyTrait<'x>,
{
    // Here the region `'c` in `<T as MyTrait<'c>>::Output` will be
    // inferred to a subset of the fn body.
    let x = bar::<T::Output>();
    drop(x);
}

fn bar<'a, T>() -> &'a ()
where
    T: 'a,
{
    &()
}

fn main() {}


