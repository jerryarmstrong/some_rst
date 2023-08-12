tests/incremental/callee_caller_cross_crate/auxiliary/a.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="rlib"]

#[cfg(rpass1)]
pub fn function0(x: u32) -> u32 {
    x
}

#[cfg(rpass2)]
pub fn function0(x: i32) -> i32 {
    x
}

pub fn function1(x: u32) {
}


