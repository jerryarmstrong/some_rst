tests/ui/regions/forall-wf-reflexive.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we consider `for<'a> T: 'a` to be sufficient to prove
// that `for<'a> T: 'a`.
//
// check-pass

#![allow(warnings)]

fn self_wf1<T>()
where
    for<'a> T: 'a,
{
    self_wf1::<T>();
}

fn main() {}


