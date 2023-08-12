tests/incremental/type_alias_cross_crate/auxiliary/a.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z query-dep-graph

#![crate_type="rlib"]

#[cfg(rpass1)]
pub type X = u32;

#[cfg(rpass2)]
pub type X = i32;

// this version doesn't actually change anything:
#[cfg(rpass3)]
pub type X = i32;

pub type Y = char;


