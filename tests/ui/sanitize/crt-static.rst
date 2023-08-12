tests/ui/sanitize/crt-static.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z sanitizer=address -C target-feature=+crt-static --target x86_64-unknown-linux-gnu
// needs-llvm-components: x86

#![feature(no_core)]
#![no_core]
#![no_main]


