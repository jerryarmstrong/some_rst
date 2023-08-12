tests/ui/imports/import-loop.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:import

use y::x;

mod y {
    pub use y::x;
}

fn main() { }


