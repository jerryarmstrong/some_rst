src/etc/test-float-parse/src/bin/many-digits.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate rand;

use rand::distributions::{Range, Sample};
use rand::{IsaacRng, Rng, SeedableRng};
use std::char;
use test_float_parse::{validate, SEED};

fn main() {
    let mut rnd = IsaacRng::from_seed(&SEED);
    let mut range = Range::new(0, 10);
    for _ in 0..5_000_000u64 {
        let num_digits = rnd.gen_range(100, 400);
        let digits = gen_digits(num_digits, &mut range, &mut rnd);
        validate(&digits);
    }
}

fn gen_digits<R: Rng>(n: u32, range: &mut Range<u32>, rnd: &mut R) -> String {
    let mut s = String::new();
    for _ in 0..n {
        let digit = char::from_digit(range.sample(rnd), 10).unwrap();
        s.push(digit);
    }
    s
}


