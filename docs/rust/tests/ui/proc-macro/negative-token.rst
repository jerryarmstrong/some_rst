tests/ui/proc-macro/negative-token.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:negative-token.rs

extern crate negative_token;

use negative_token::*;

fn main() {
    assert_eq!(-1, neg_one!());
    assert_eq!(-1.0, neg_one_float!());
}


