tests/ui/cross-crate/cross-crate-const-pat.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:cci_const.rs

// pretty-expanded FIXME #23616

extern crate cci_const;

pub fn main() {
    let x = cci_const::uint_val;
    match x {
        cci_const::uint_val => {}
        _ => {}
    }
}


