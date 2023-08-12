tests/ui/macros/macro-crate-def-only.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:macro_crate_def_only.rs


#[macro_use] #[no_link]
extern crate macro_crate_def_only;

pub fn main() {
    assert_eq!(5, make_a_5!());
}


