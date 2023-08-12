src/tools/miri/tests/fail/breakpoint.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

fn main() {
    unsafe {
        core::intrinsics::breakpoint() //~ ERROR: Trace/breakpoint trap
    };
}


