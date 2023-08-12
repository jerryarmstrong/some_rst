src/tools/miri/tests/many-seeds/scoped-thread-leak.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Regression test for https://github.com/rust-lang/miri/issues/2629
use std::thread;

fn main() {
    thread::scope(|s| {
        s.spawn(|| {});
    });
}


