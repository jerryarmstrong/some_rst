tests/ui/issues/issue-1660.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

// pretty-expanded FIXME #23616

pub fn main() {
    static _x: isize = 1<<2;
}


