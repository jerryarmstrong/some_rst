tests/ui/rfc-2632-const-trait-impl/std-impl-gate.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This tests feature gates for const impls in the standard library.

// revisions: stock gated
//[gated] run-pass

#![cfg_attr(gated, feature(const_trait_impl, const_default_impls))]

fn non_const_context() -> Vec<usize> {
    Default::default()
}

const fn const_context() -> Vec<usize> {
    Default::default()
    //[stock]~^ ERROR cannot call non-const fn
}

fn main() {
    const VAL: Vec<usize> = const_context();

    assert_eq!(VAL, non_const_context());
}


