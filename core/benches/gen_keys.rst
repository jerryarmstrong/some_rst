core/benches/gen_keys.rs
========================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![feature(test)]

extern crate test;

use {solana_core::gen_keys::GenKeys, test::Bencher};

#[bench]
fn bench_gen_keys(b: &mut Bencher) {
    let mut rnd = GenKeys::new([0u8; 32]);
    b.iter(|| rnd.gen_n_keypairs(1000));
}


