tests/ui/parser/issues/issue-88583-union-as-ident.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(non_camel_case_types)]

struct union;

impl union {
    pub fn new() -> Self {
        union { }
    }
}

fn main() {
    let _u = union::new();
}


