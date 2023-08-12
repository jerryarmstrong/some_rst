src/tools/miri/tests/panic/div-by-zero-2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unconditional_panic)]

fn main() {
    let _n = 1 / 0;
}


