tests/ui/functions-closures/fn-coerce-field.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616
#![allow(non_camel_case_types)]

struct r<F> where F: FnOnce() {
    field: F,
}

pub fn main() {
    fn f() {}
    let _i: r<fn()> = r {field: f as fn()};
}


