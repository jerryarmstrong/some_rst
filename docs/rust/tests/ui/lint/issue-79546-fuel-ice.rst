tests/ui/lint/issue-79546-fuel-ice.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for the ICE described in #79546.

// compile-flags: --cap-lints=allow -Zfuel=issue79546=0
// check-pass
#![crate_name="issue79546"]

struct S;
fn main() {}


