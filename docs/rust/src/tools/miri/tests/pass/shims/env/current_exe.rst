src/tools/miri/tests/pass/shims/env/current_exe.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@only-on-host: the Linux std implementation opens /proc/self/exe, which doesn't work cross-target
//@compile-flags: -Zmiri-disable-isolation
use std::env;

fn main() {
    // The actual value we get is a bit odd: we get the Miri binary that interprets us.
    env::current_exe().unwrap();
}


