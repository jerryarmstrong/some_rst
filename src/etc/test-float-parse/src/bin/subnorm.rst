src/etc/test-float-parse/src/bin/subnorm.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::transmute;
use test_float_parse::validate;

fn main() {
    for bits in 0u32..(1 << 21) {
        let single: f32 = unsafe { transmute(bits) };
        validate(&format!("{:e}", single));
        let double: f64 = unsafe { transmute(bits as u64) };
        validate(&format!("{:e}", double));
    }
}


