tests/ui/try-operator-hygiene.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_upper_case_globals)]
#![allow(dead_code)]
// `expr?` expands to:
//
// match expr {
//     Ok(val) => val,
//     Err(err) => return Err(From::from(err)),
// }
//
// This test verifies that the expansion is hygienic, i.e., it's not affected by other `val` and
// `err` bindings that may be in scope.

use std::num::ParseIntError;

fn main() {
    assert_eq!(parse(), Ok(1));
}

fn parse() -> Result<i32, ParseIntError> {
    const val: char = 'a';
    const err: char = 'b';

    Ok("1".parse::<i32>()?)
}


