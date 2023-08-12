tests/ui/issues/issue-8259.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_upper_case_globals)]

// aux-build:issue-8259.rs

// pretty-expanded FIXME #23616

extern crate issue_8259 as other;
static a: other::Foo<'static> = other::Foo::A;

pub fn main() {}


