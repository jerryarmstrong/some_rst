tests/ui/deprecation/atomic_initializers.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// check-pass

#[allow(deprecated, unused_imports)]
use std::sync::atomic::{AtomicIsize, ATOMIC_ISIZE_INIT};

#[allow(dead_code)]
static FOO: AtomicIsize = ATOMIC_ISIZE_INIT;
//~^ WARN use of deprecated constant

fn main() {}


