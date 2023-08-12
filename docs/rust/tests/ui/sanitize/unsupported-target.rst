tests/ui/sanitize/unsupported-target.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z sanitizer=leak --target i686-unknown-linux-gnu
// needs-llvm-components: x86
// error-pattern: error: leak sanitizer is not supported for this target
#![feature(no_core)]
#![no_core]
#![no_main]


