tests/ui/test-attrs/test-main-not-dead.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --test

#![deny(dead_code)]

fn main() { panic!(); }


