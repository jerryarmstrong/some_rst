tests/ui/imports/extern-crate-self/extern-crate-self-fail.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate self; //~ ERROR `extern crate self;` requires renaming

#[macro_use] //~ ERROR `#[macro_use]` is not supported on `extern crate self`
extern crate self as foo;

fn main() {}


