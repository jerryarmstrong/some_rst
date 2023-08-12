tests/ui/issues/issue-9249.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

static DATA:&'static [&'static str] = &["my string"];
fn main() { }


