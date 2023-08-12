tests/ui/async-await/await-sequence.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// compile-flags: -Z drop-tracking
// build-pass

use std::collections::HashMap;

fn main() {
    let _ = real_main();
}

async fn nop() {}

async fn real_main() {
    nop().await;
    nop().await;
    nop().await;
    nop().await;

    let mut map: HashMap<(), ()> = HashMap::new();
    map.insert((), nop().await);
}


