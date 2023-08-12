tests/ui/panic-handler/panic-handler-missing.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // dont-check-compiler-stderr
// error-pattern: `#[panic_handler]` function required, but not found

#![feature(lang_items)]
#![no_main]
#![no_std]

#[lang = "eh_personality"]
fn eh() {}


