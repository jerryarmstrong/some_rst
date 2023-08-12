tests/rustdoc-ui/feature-gate-rustdoc_missing_doc_code_examples.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unknown_lints)]
//~^ NOTE defined here

#![allow(rustdoc::missing_doc_code_examples)]
//~^ ERROR unknown lint
//~| ERROR unknown lint
//~| NOTE lint is unstable
//~| NOTE lint is unstable
//~| NOTE see issue
//~| NOTE see issue


