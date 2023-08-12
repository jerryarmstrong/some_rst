src/tools/miri/tests/panic/panic1.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@rustc-env: RUST_BACKTRACE=1
//@compile-flags: -Zmiri-disable-isolation

fn main() {
    std::panic!("panicking from libstd");
}


