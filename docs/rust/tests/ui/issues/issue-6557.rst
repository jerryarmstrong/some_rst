tests/ui/issues/issue-6557.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

#![feature(box_patterns)]

fn foo(box (_x, _y): Box<(isize, isize)>) {}

pub fn main() {}


