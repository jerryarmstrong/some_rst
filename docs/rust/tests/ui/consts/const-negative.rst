tests/ui/consts/const-negative.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #358
#![allow(non_upper_case_globals)]

static toplevel_mod: isize = -1;

pub fn main() {
    assert_eq!(toplevel_mod, -1);
}


