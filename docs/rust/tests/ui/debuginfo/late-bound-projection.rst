tests/ui/debuginfo/late-bound-projection.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags: -Cdebuginfo=2 --crate-type=rlib
// Fixes issue #94998

pub trait Trait {}

pub fn run(_: &dyn FnOnce(&()) -> Box<dyn Trait + '_>) {}


