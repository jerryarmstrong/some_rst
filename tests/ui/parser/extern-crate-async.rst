tests/ui/parser/extern-crate-async.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we don't parse `extern crate async`
// the front matter of a function leading us astray.

// check-pass

fn main() {}

#[cfg(FALSE)]
extern crate async;

#[cfg(FALSE)]
extern crate async as something_else;


