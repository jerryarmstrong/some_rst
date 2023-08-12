tests/ui/proc-macro/derive-helper-configured.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Derive helpers are resolved successfully inside `cfg_attr`.

// check-pass
// compile-flats:--cfg TRUE
// aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

#[cfg_attr(TRUE, empty_helper)]
#[derive(Empty)]
#[cfg_attr(TRUE, empty_helper)]
struct S {
    #[cfg_attr(TRUE, empty_helper)]
    field: u8,
}

fn main() {}


