tests/ui/imports/issue-26873-multifile/issue-26873-multifile.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(non_snake_case)]

// ignore-pretty issue #37195

#[path = "issue-26873-multifile/mod.rs"]
mod multifile;

fn main() {}


