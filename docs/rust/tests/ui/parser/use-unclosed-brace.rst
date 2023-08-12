tests/ui/parser/use-unclosed-brace.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: expected one of `,`, `::`, `as`, or `}`, found `;`
// error-pattern: this file contains an unclosed delimiter
// error-pattern: expected item, found `}`
use foo::{bar, baz;

use std::fmt::Display;

mod bar { }

mod baz { }

fn main() {}


