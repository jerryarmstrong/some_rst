src/tools/miri/tests/panic/overflowing-rsh-1.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(arithmetic_overflow)]

fn main() {
    let _n = 1i64 >> 64;
}


