tests/pretty/attr-fn-inner.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing that both the inner item and next outer item are
// preserved, and that the first outer item parsed in main is not
// accidentally carried over to each inner function

// pp-exact

#![feature(rustc_attrs)]

fn main() {
    #![rustc_dummy]
    #[rustc_dummy]
    fn f() {}

    #[rustc_dummy]
    fn g() {}
}


