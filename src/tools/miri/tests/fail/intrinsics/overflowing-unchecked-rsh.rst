src/tools/miri/tests/fail/intrinsics/overflowing-unchecked-rsh.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unchecked_math)]

fn main() {
    unsafe {
        let _n = 1i64.unchecked_shr(64);
        //~^ ERROR: overflowing shift by 64 in `unchecked_shr`
    }
}


