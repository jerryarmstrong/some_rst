tests/incremental/macro_export.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail1 cfail2 cfail3
// build-pass (FIXME(62277): could be check-pass?)

// This test case makes sure that we can compile with incremental compilation
// enabled when there are macros exported from this crate. (See #37756)

#![crate_type="rlib"]

#[macro_export]
macro_rules! some_macro {
    ($e:expr) => ($e + 1)
}


