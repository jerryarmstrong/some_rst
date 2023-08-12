tests/ui/cfg/cfg-attr-crate.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// https://github.com/rust-lang/rust/issues/21833#issuecomment-72353044

// pretty-expanded FIXME #23616

#![cfg_attr(not_used, no_core)]

fn main() { }


