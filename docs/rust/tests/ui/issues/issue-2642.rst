tests/ui/issues/issue-2642.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn f() {
   let _x: usize = loop { loop { break; } };
}

pub fn main() {
}


