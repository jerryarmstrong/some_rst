src/tools/miri/tests/panic/overflowing-lsh-neg.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(arithmetic_overflow)]

fn main() {
    let _n = 2i64 << -1;
}


