tests/ui/issues/issue-1821.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// Issue #1821 - Don't recurse trying to typecheck this


// pretty-expanded FIXME #23616

enum t {
    foo(Vec<t>)
}
pub fn main() {}


