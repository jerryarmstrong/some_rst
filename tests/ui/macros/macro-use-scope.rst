tests/ui/macros/macro-use-scope.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:two_macros.rs

// build-pass (FIXME(62277): could be check-pass?)
#![allow(unused)]

fn f() {
    let _ = macro_one!();
}
#[macro_use(macro_one)] // Check that this macro is usable in the above function
extern crate two_macros;

fn g() {
    macro_two!();
}
macro_rules! m { () => {
    #[macro_use(macro_two)] // Check that this macro is usable in the above function
    extern crate two_macros as _two_macros;
} }
m!();


fn main() {}


