src/tools/miri/tests/pass/backtrace/backtrace-global-alloc.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-isolation
//@rustc-env: RUST_BACKTRACE=1

use std::alloc::System;
use std::backtrace::Backtrace;

#[global_allocator]
static GLOBAL_ALLOCATOR: System = System;

fn main() {
    eprint!("{}", Backtrace::capture());
}


