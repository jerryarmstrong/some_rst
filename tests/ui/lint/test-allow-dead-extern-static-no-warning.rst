tests/ui/lint/test-allow-dead-extern-static-no-warning.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --test

#![deny(dead_code)]

extern "C" {
    #[allow(dead_code)]
    static Qt: u64;
}

fn main() {}


