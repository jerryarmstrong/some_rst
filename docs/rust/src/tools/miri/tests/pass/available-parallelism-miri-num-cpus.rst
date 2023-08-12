src/tools/miri/tests/pass/available-parallelism-miri-num-cpus.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-num-cpus=1024

use std::num::NonZeroUsize;
use std::thread::available_parallelism;

fn main() {
    assert_eq!(available_parallelism().unwrap(), NonZeroUsize::new(1024).unwrap());
}


