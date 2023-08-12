tests/ui/rust-2018/uniform-paths/prelude-fail.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// Tool attribute
use rustfmt::skip as imported_rustfmt_skip; //~ ERROR unresolved import `rustfmt`

fn main() {}


