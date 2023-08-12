tests/ui/consts/issue-6991.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
#![allow(non_upper_case_globals)]

static x: &'static usize = &1;
static y: usize = *x;

fn main() {}


