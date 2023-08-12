src/tools/miri/tests/pass/getpid.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-isolation

fn getpid() -> u32 {
    std::process::id()
}

fn main() {
    getpid();
}


