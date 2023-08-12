src/tools/miri/tests/fail/type-too-large.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-32bit

fn main() {
    let _fat: [u8; (1 << 61) + (1 << 31)];
    _fat = [0; (1u64 << 61) as usize + (1u64 << 31) as usize]; //~ ERROR: post-monomorphization error
}


