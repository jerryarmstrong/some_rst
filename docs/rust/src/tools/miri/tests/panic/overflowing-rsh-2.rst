src/tools/miri/tests/panic/overflowing-rsh-2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(arithmetic_overflow)]

fn main() {
    // Make sure we catch overflows that would be hidden by first casting the RHS to u32
    let _n = 1i64 >> (u32::MAX as i64 + 1);
}


