src/tools/miri/tests/pass/memleak_ignored.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-ignore-leaks

fn main() {
    std::mem::forget(Box::new(42));
}


