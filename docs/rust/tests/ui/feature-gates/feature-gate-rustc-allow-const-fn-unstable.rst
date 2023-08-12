tests/ui/feature-gates/feature-gate-rustc-allow-const-fn-unstable.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_macros)]

#[rustc_allow_const_fn_unstable()] //~ ERROR rustc_allow_const_fn_unstable side-steps
const fn foo() { }

fn main() {}


