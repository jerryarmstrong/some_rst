src/tools/rustfmt/tests/target/imports/imports-reorder-lines-and-items.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cmp::{a, b, c, d};
use std::ddd::aaa;
use std::ddd::{a, b, c as g, d as p};
/// This comment should stay with `use std::str;`
use std::str;
// This comment should stay with `use std::ddd:bbb;`
use std::ddd::bbb;


