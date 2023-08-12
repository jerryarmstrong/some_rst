tests/ui/panic-runtime/two-panic-runtimes.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// dont-check-compiler-stderr
// error-pattern:cannot link together two panic runtimes: panic_runtime_unwind and panic_runtime_unwind2
// aux-build:panic-runtime-unwind.rs
// aux-build:panic-runtime-unwind2.rs
// aux-build:panic-runtime-lang-items.rs

#![no_std]
#![no_main]

extern crate panic_runtime_unwind;
extern crate panic_runtime_unwind2;
extern crate panic_runtime_lang_items;

fn main() {}


