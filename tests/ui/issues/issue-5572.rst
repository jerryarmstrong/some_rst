tests/ui/issues/issue-5572.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn foo<T: ::std::cmp::PartialEq>(_t: T) { }

pub fn main() { }


