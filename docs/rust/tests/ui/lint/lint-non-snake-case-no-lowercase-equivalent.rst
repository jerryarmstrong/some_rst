tests/ui/lint/lint-non-snake-case-no-lowercase-equivalent.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(dead_code)]
// pretty-expanded FIXME #23616

#![deny(non_snake_case)]

// This name is neither upper nor lower case
fn 你好() {}

fn main() {}


