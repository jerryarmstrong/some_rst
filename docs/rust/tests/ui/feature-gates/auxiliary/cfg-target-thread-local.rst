tests/ui/feature-gates/auxiliary/cfg-target-thread-local.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(thread_local)]
#![feature(cfg_target_thread_local)]
#![crate_type = "lib"]

#[no_mangle]
#[cfg_attr(target_thread_local, thread_local)]
pub static FOO: u32 = 3;


