tests/ui/issues/issue-4208.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// aux-build:issue-4208-cc.rs

// pretty-expanded FIXME #23616

extern crate numeric;
use numeric::{sin, Angle};

fn foo<T, A:Angle<T>>(theta: A) -> T { sin(&theta) }

pub fn main() {}


