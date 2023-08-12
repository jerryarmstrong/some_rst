src/tools/rustfmt/tests/target/issue-691.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true

//! `std` or `core` and simply link to this library. In case the target
//! platform has no hardware
//! support for some operation, software implementations provided by this
//! library will be used automagically.
// TODO: provide instructions to override default libm link and how to link to
// this library.
fn foo() {}


