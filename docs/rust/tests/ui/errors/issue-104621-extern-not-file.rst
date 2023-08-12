tests/ui/errors/issue-104621-extern-not-file.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --extern foo=.

extern crate foo; //~ ERROR extern location for foo is not a file: .
fn main() {}


