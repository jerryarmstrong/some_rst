tests/ui/consts/min_const_fn/allow_raw_ptr_dereference_const_fn.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::ptr;

const fn test_fn(x: *const i32) {
    let x2 = unsafe { ptr::addr_of!(*x) };
}

fn main() {}


