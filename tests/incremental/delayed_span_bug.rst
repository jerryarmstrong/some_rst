tests/incremental/delayed_span_bug.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail1 cfail2
// should-ice
// error-pattern: delayed span bug triggered by #[rustc_error(delay_span_bug_from_inside_query)]

#![feature(rustc_attrs)]

#[rustc_error(delay_span_bug_from_inside_query)]
fn main() {}


