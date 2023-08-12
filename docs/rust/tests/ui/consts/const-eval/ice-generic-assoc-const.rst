tests/ui/consts/const-eval/ice-generic-assoc-const.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (tests post-monomorphisation failure)
#![crate_type = "lib"]

pub trait Nullable {
    const NULL: Self;

    fn is_null(&self) -> bool;
}

impl<T> Nullable for *const T {
    const NULL: Self = core::ptr::null::<T>();

    fn is_null(&self) -> bool {
        *self == Self::NULL
    }
}


