tests/ui/threads-sendsync/auxiliary/thread-local-extern-static.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(cfg_target_thread_local, thread_local)]
#![crate_type = "lib"]

#[cfg(target_thread_local)]
use std::cell::Cell;

#[no_mangle]
#[cfg(target_thread_local)]
#[thread_local]
pub static FOO: Cell<u32> = Cell::new(3);


