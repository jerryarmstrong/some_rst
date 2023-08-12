tests/ui/panic-runtime/want-unwind-got-abort.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// needs-unwind
// error-pattern:is not compiled with this crate's panic strategy `unwind`
// aux-build:panic-runtime-abort.rs
// aux-build:panic-runtime-lang-items.rs

#![no_std]
#![no_main]

extern crate panic_runtime_abort;
extern crate panic_runtime_lang_items;


