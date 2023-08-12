src/etc/test-float-parse/src/bin/rand-f64.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate rand;

use rand::{IsaacRng, Rng, SeedableRng};
use std::mem::transmute;
use test_float_parse::{validate, SEED};

fn main() {
    let mut rnd = IsaacRng::from_seed(&SEED);
    let mut i = 0;
    while i < 10_000_000 {
        let bits = rnd.next_u64();
        let x: f64 = unsafe { transmute(bits) };
        if x.is_finite() {
            validate(&format!("{:e}", x));
            i += 1;
        }
    }
}


