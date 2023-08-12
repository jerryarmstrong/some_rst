tests/ui/feature-gates/issue-43106-gating-of-test.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The non-crate level cases are in issue-43106-gating-of-builtin-attrs.rs.

#![allow(soft_unstable)]
#![test                    = "4200"]
//~^ ERROR cannot determine resolution for the attribute macro `test`
//~^^ ERROR `test` attribute cannot be used at crate level
fn main() {}


