tests/ui/deriving/deriving-in-macro.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(non_camel_case_types)]

macro_rules! define_vec {
    () => (
        mod foo {
            #[derive(PartialEq)]
            pub struct bar;
        }
    )
}

define_vec![];

pub fn main() {}


