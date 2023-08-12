tests/ui/impl-trait/return-position-impl-trait-minimal.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

fn main() {}

fn foo() -> impl std::fmt::Debug { "cake" }


