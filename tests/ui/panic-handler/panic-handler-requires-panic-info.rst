tests/ui/panic-handler/panic-handler-requires-panic-info.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort
// error-pattern: language item required, but not found: `panic_info`

#![feature(lang_items)]
#![feature(no_core)]
#![no_core]
#![no_main]

#[panic_handler]
fn panic() -> ! {
    loop {}
}

#[lang = "sized"]
trait Sized {}


