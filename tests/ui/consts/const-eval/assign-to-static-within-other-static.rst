tests/ui/consts/const-eval/assign-to-static-within-other-static.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // New test for #53818: modifying static memory at compile-time is not allowed.
// The test should never compile successfully

use std::cell::UnsafeCell;

static mut FOO: u32 = 42;
static BOO: () = unsafe {
    FOO = 5;
    //~^ could not evaluate static initializer [E0080]
};

fn main() {}


