tests/ui/panic-runtime/transitive-link-a-bunch.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// needs-unwind
// aux-build:panic-runtime-unwind.rs
// aux-build:panic-runtime-abort.rs
// aux-build:wants-panic-runtime-unwind.rs
// aux-build:wants-panic-runtime-abort.rs
// aux-build:panic-runtime-lang-items.rs
// error-pattern: is not compiled with this crate's panic strategy `unwind`

#![no_std]
#![no_main]

extern crate wants_panic_runtime_unwind;
extern crate wants_panic_runtime_abort;
extern crate panic_runtime_lang_items;


