src/tools/clippy/tests/ui/borrow_interior_mutable_const/auxiliary/helper.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // this file solely exists to test constants defined in foreign crates.
// As the most common case is the `http` crate, it replicates `http::HeadewrName`'s structure.

#![allow(clippy::declare_interior_mutable_const)]
#![allow(unused_tuple_struct_fields)]

use std::sync::atomic::AtomicUsize;

enum Private<T> {
    ToBeUnfrozen(T),
    Frozen(usize),
}

pub struct Wrapper(Private<AtomicUsize>);

pub const WRAPPED_PRIVATE_UNFROZEN_VARIANT: Wrapper = Wrapper(Private::ToBeUnfrozen(AtomicUsize::new(6)));
pub const WRAPPED_PRIVATE_FROZEN_VARIANT: Wrapper = Wrapper(Private::Frozen(7));


