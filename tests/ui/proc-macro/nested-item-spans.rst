tests/ui/proc-macro/nested-item-spans.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

#[recollect_attr]
fn another() {
    fn bar() {
        let x: u32 = "x"; //~ ERROR: mismatched types
    }

    bar();
}

fn main() {
    #[recollect_attr]
    fn bar() {
        let x: u32 = "x"; //~ ERROR: mismatched types
    }

    bar();
    another();
}


