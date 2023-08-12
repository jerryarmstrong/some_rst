tests/ui/consts/const-region-ptrs-noncopy.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_upper_case_globals)]

type Big = [u64; 8];
struct Pair<'a> { a: isize, b: &'a Big }
const x: &'static Big = &([13, 14, 10, 13, 11, 14, 14, 15]);
const y: &'static Pair<'static> = &Pair {a: 15, b: x};

pub fn main() {
    assert_eq!(x as *const Big, y.b as *const Big);
}


