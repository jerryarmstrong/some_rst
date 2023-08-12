tests/ui/feature-gates/feature-gate-cfg-target-thread-local.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-windows
// aux-build:cfg-target-thread-local.rs

#![feature(thread_local)]

extern crate cfg_target_thread_local;

extern "C" {
    #[cfg_attr(target_thread_local, thread_local)]
    //~^ `cfg(target_thread_local)` is experimental and subject to change
    static FOO: u32;
}

fn main() {
    assert_eq!(FOO, 3);
}


