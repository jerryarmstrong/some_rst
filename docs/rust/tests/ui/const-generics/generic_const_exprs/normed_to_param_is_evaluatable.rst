tests/ui/const-generics/generic_const_exprs/normed_to_param_is_evaluatable.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features, unused_braces)]

#[rustfmt::skip]
fn foo<const N: usize>() {
    bar::<{{{{{{ N }}}}}}>();
}

fn bar<const N: usize>() {}

fn main() {}


