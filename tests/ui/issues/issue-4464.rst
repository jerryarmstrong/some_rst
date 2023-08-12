tests/ui/issues/issue-4464.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn broken(v: &[u8], i: usize, j: usize) -> &[u8] { &v[i..j] }

pub fn main() {}


