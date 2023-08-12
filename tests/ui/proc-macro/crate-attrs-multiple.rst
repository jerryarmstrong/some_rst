tests/ui/proc-macro/crate-attrs-multiple.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Multiple custom crate-level attributes, both inert and active.

// check-pass
// aux-crate:test_macros=test-macros.rs

#![feature(custom_inner_attributes)]
#![feature(prelude_import)]

#![test_macros::identity_attr]
#![rustfmt::skip]
#![test_macros::identity_attr]
#![rustfmt::skip]

fn main() {}


