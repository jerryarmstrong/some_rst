tests/ui/rfc-2632-const-trait-impl/feature-gate.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: stock gated
// gate-test-const_trait_impl

#![cfg_attr(gated, feature(const_trait_impl))]
#![feature(rustc_attrs)]

struct S;
#[const_trait] //[stock]~ ERROR `const_trait` is a temporary placeholder
trait T {}
impl const T for S {}
//[stock]~^ ERROR const trait impls are experimental

#[rustc_error]
fn main() {} //[gated]~ ERROR fatal error triggered by #[rustc_error]


