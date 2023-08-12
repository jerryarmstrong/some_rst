tests/ui/feature-gates/issue-49983-see-issue-0.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate core;

// error should not say "(see issue #0)"
#[allow(unused_imports)] use core::ptr::Unique; //~ ERROR use of unstable library feature

fn main() {}


