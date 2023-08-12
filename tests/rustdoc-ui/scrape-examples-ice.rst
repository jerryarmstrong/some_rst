tests/rustdoc-ui/scrape-examples-ice.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options --scrape-examples-output-path {{build-base}}/t.calls --scrape-examples-target-crate foobar
// check-pass
#![no_std]
use core as _;


