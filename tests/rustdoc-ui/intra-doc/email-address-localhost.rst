tests/rustdoc-ui/intra-doc/email-address-localhost.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "nightly|beta|1\.[0-9][0-9]\.[0-9]" -> "$$CHANNEL"
// check-pass
#![deny(warnings)]

//! Email me at <hello@localhost>.

//! This should *not* warn: <hello@example.com>.


