tests/ui/regions/forall-wf-ref-reflexive.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we consider `for<'a> &'a T: 'a` to be sufficient to prove
// that `for<'a> &'a T: 'a`.
//
// FIXME. Except we don't!

#![allow(warnings)]

fn self_wf2<T>()
where
    for<'a> &'a T: 'a,
{
    self_wf2::<T>();
    //~^ ERROR `T` does not live long enough
    //
    // FIXME. This ought to be accepted, presumably.
}

fn main() {}


