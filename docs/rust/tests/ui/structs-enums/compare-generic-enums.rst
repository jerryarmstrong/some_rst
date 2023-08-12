tests/ui/structs-enums/compare-generic-enums.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]


type an_int = isize;

fn cmp(x: Option<an_int>, y: Option<isize>) -> bool {
    x == y
}

pub fn main() {
    assert!(!cmp(Some(3), None));
    assert!(!cmp(Some(3), Some(4)));
    assert!(cmp(Some(3), Some(3)));
    assert!(cmp(None, None));
}


