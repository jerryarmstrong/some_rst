src/tools/miri/tests/fail/const-ub-checks.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_ptr_read)]

const UNALIGNED_READ: () = unsafe {
    let x = &[0u8; 4];
    let ptr = x.as_ptr().cast::<u32>();
    ptr.read(); //~ERROR: evaluation of constant value failed
};

fn main() {
    let _x = UNALIGNED_READ;
}


