language/benchmarks/benches/transactions.rs
===========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use criterion::{criterion_group, criterion_main, Criterion};
use proptest::prelude::*;
use solana_libra_language_benchmarks::transactions::TransactionBencher;
use solana_libra_language_e2e_tests::account_universe::P2PTransferGen;

fn peer_to_peer(c: &mut Criterion) {
    c.bench_function("peer_to_peer", |b| {
        let bencher = TransactionBencher::new(any_with::<P2PTransferGen>((1_000, 1_000_000)));
        bencher.bench(b)
    });
}

criterion_group!(benches, peer_to_peer);
criterion_main!(benches);


