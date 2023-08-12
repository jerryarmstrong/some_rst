tests/ui/function-pointer/sized-ret-with-binder.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(unboxed_closures)]

fn is_fn<T: for<'a> Fn<(&'a (),)>>() {}
fn is_fn2<T: for<'a, 'b> Fn<(&'a &'b (),)>>() {}

struct Outlives<'a, 'b>(std::marker::PhantomData<&'a &'b ()>);

fn main() {
    is_fn::<for<'a> fn(&'a ()) -> &'a ()>();
    is_fn::<for<'a> fn(&'a ()) -> &'a dyn std::fmt::Debug>();
    is_fn2::<for<'a, 'b> fn(&'a &'b ()) -> Outlives<'a, 'b>>();
    is_fn2::<for<'a, 'b> fn(&'a &'b ()) -> (&'a (), &'a ())>();
}


