tests/ui/proc-macro/import.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

extern crate test_macros;

use test_macros::empty_derive;
//~^ ERROR: unresolved import `test_macros::empty_derive`

fn main() {}


