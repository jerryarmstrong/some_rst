tests/ui/issues/issue-8506.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(non_upper_case_globals)]

#![allow(dead_code)]

enum Either {
    One,
    Other(String,String)
}

static one : Either = Either::One;

pub fn main () { }


