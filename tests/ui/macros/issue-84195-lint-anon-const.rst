tests/ui/macros/issue-84195-lint-anon-const.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #84195
// Checks that we properly fire lints that occur inside
// anon consts.

#![deny(semicolon_in_expressions_from_macros)]

macro_rules! len {
    () => { 0; }; //~  ERROR trailing semicolon
                  //~| WARN this was previously accepted
}

fn main() {
    let val: [u8; len!()] = [];
}


