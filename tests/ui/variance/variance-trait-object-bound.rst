tests/ui/variance/variance-trait-object-bound.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that regions which appear in a trait object type are
// observed by the variance inference algorithm (and hence
// `TOption` is contavariant w/r/t `'a` and not bivariant).
//
// Issue #18262.

#![feature(rustc_attrs)]

use std::mem;

trait T { fn foo(&self); }

#[rustc_variance]
struct TOption<'a> { //~ ERROR [-]
    v: Option<Box<dyn T + 'a>>,
}

fn main() { }


