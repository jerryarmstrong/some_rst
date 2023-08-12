tests/ui/underscore-lifetime/in-fn-return-illegal.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that the `'_` used in structs/enums gives an error.

use std::fmt::Debug;

fn foo(x: &u32, y: &u32) -> &'_ u32 { loop { } } //~ ERROR missing lifetime specifier

fn main() { }


