tests/ui/issues/issue-9243.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(dead_code)]
// Regression test for issue 9243
#![allow(non_upper_case_globals)]

pub struct Test {
    mem: isize,
}

pub static g_test: Test = Test {mem: 0};

impl Drop for Test {
    fn drop(&mut self) {}
}

fn main() {}


