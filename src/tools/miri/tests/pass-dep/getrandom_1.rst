src/tools/miri/tests/pass-dep/getrandom_1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // mac-os `getrandom_1` does some pointer shenanigans
//@compile-flags: -Zmiri-permissive-provenance

/// Test old version of `getrandom`.
fn main() {
    let mut data = vec![0; 16];
    getrandom_1::getrandom(&mut data).unwrap();
}


