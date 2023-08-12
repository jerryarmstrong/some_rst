src/tools/miri/tests/pass-dep/tokio_mvp.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Need to disable preemption to stay on the supported MVP codepath in mio.
//@compile-flags: -Zmiri-disable-isolation -Zmiri-permissive-provenance -Zmiri-preemption-rate=0
//@only-target-x86_64-unknown-linux: support for tokio exists only on linux and x86

#[tokio::main]
async fn main() {}


