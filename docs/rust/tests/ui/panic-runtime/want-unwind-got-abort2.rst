tests/ui/panic-runtime/want-unwind-got-abort2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// needs-unwind
// error-pattern:is incompatible with this crate's strategy of `unwind`
// aux-build:panic-runtime-abort.rs
// aux-build:wants-panic-runtime-abort.rs
// aux-build:panic-runtime-lang-items.rs

#![no_std]
#![no_main]

extern crate wants_panic_runtime_abort;
extern crate panic_runtime_lang_items;


