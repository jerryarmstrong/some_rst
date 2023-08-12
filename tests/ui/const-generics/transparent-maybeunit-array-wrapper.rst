tests/ui/const-generics/transparent-maybeunit-array-wrapper.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: full min

#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

use std::mem::MaybeUninit;

#[repr(transparent)]
pub struct MaybeUninitWrapper<const N: usize>(MaybeUninit<[u64; N]>);

fn main() {}


