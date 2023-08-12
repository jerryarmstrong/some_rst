crossbeam-skiplist/examples/simple.rs
=====================================

Last edited: 2022-07-31 15:42:50

Contents:

.. code-block:: rs

    // use std::time::Instant;

fn main() {
    // let map = crossbeam_skiplist::SkipMap::new();
    // // let mut map = std::collections::BTreeMap::new();
    // // let mut map = std::collections::HashMap::new();
    //
    // let now = Instant::now();
    //
    // let mut num = 0u64;
    // for _ in 0..1_000_000 {
    //     num = num.wrapping_mul(17).wrapping_add(255);
    //     map.insert(num, !num);
    // }
    //
    // let dur = Instant::now() - now;
    // println!("insert: {} sec", dur.as_secs() as f64 + dur.subsec_nanos() as f64 * 1e-9);
    //
    // let now = Instant::now();
    //
    // for _ in map.iter() {}
    //
    // let dur = Instant::now() - now;
    // println!("iterate: {} sec", dur.as_secs() as f64 + dur.subsec_nanos() as f64 * 1e-9);
}


