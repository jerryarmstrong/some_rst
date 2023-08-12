tests/ui/issues/issue-5900.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

pub mod foo {
    use super::Bar;

    pub struct FooStruct { bar : Bar }
}

pub enum Bar {
    Bar0 = 0 as isize
}

pub fn main() {}


