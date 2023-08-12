tests/ui/lint/lint-non-camel-case-with-trailing-underscores.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(dead_code)]
// This is ok because we often use the trailing underscore to mean 'prime'

// pretty-expanded FIXME #23616

#[forbid(non_camel_case_types)]
type Foo_ = isize;

pub fn main() { }


