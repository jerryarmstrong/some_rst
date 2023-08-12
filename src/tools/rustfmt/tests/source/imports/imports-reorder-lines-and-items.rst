src/tools/rustfmt/tests/source/imports/imports-reorder-lines-and-items.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// This comment should stay with `use std::str;`
use std::str;
use std::cmp::{d, c, b, a};
use std::ddd::aaa;
use std::ddd::{d as p, c as g, b, a};
// This comment should stay with `use std::ddd:bbb;`
use std::ddd::bbb;


