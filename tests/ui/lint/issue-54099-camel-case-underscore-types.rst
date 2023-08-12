tests/ui/lint/issue-54099-camel-case-underscore-types.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![forbid(non_camel_case_types)]
#![allow(dead_code)]

// None of the following types should generate a warning
struct _X {}
struct __X {}
struct __ {}
struct X_ {}
struct X__ {}
struct X___ {}

fn main() { }


