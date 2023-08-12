tests/ui/deriving/deriving-enum-single-variant.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(non_camel_case_types)]

pub type task_id = isize;

#[derive(PartialEq)]
pub enum Task {
    TaskHandle(task_id)
}

pub fn main() { }


