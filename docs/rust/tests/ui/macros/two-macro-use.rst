tests/ui/macros/two-macro-use.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:two_macros.rs

#[macro_use(macro_one)]
#[macro_use(macro_two)]
extern crate two_macros;

pub fn main() {
    macro_one!();
    macro_two!();
}


