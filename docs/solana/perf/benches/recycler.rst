perf/benches/recycler.rs
========================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![feature(test)]

extern crate test;

use {
    solana_perf::{packet::PacketBatchRecycler, recycler::Recycler},
    test::Bencher,
};

#[bench]
fn bench_recycler(bencher: &mut Bencher) {
    solana_logger::setup();

    let recycler: PacketBatchRecycler = Recycler::default();

    for _ in 0..1000 {
        let _packet = recycler.allocate("");
    }

    bencher.iter(move || {
        let _packet = recycler.allocate("");
    });
}


