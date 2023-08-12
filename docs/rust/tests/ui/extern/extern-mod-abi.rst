tests/ui/extern/extern-mod-abi.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

extern "C" {
    fn pow(x: f64, y: f64) -> f64;
}

pub fn main() {}


