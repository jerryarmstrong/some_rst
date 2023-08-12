tests/ui/early-ret-binop-add.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
#![allow(unreachable_code)]
// pretty-expanded FIXME #23616

use std::ops::Add;

fn wsucc<T:Add<Output=T> + Copy>(n: T) -> T { n + { return n } }

pub fn main() { }


