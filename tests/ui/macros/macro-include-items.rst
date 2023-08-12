tests/ui/macros/macro-include-items.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

// ignore-pretty issue #37195

fn bar() {}

include!(concat!("", "", "auxiliary/", "macro-include-items-item.rs"));

fn main() {
    foo();
    assert_eq!(include!(concat!("", "auxiliary/", "macro-include-items-expr.rs")), 1_usize);
}


