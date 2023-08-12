tests/run-make-fulldeps/extern-fn-with-union/test.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate testcrate;

use std::mem;

extern "C" {
    fn give_back(tu: testcrate::TestUnion) -> u64;
}

fn main() {
    let magic: u64 = 0xDEADBEEF;

    // Let's test calling it cross crate
    let back = unsafe { testcrate::give_back(mem::transmute(magic)) };
    assert_eq!(magic, back);

    // And just within this crate
    let back = unsafe { give_back(mem::transmute(magic)) };
    assert_eq!(magic, back);
}


