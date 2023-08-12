tests/ui/consts/min_const_fn/min_const_fn_unsafe_bad.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const fn bad_const_fn_deref_raw(x: *mut usize) -> &'static usize { unsafe { &*x } }
//~^ dereferencing raw mutable pointers in constant functions

const unsafe fn bad_const_unsafe_deref_raw(x: *mut usize) -> usize { *x }
//~^ dereferencing raw mutable pointers in constant functions

const unsafe fn bad_const_unsafe_deref_raw_ref(x: *mut usize) -> &'static usize { &*x }
//~^ dereferencing raw mutable pointers in constant functions

fn main() {}


