tests/ui/const-generics/const-argument-non-static-lifetime.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // [full] check-pass
// revisions: full min

// regression test for #78180
// compile-flags: -Zsave-analysis

#![cfg_attr(full, feature(generic_const_exprs))]
#![cfg_attr(full, allow(incomplete_features))]
#![allow(dead_code)]

fn test<const N: usize>() {}

fn wow<'a>() -> &'a () {
    test::<{
        let _: &'a (); //[min]~ ERROR a non-static lifetime
        3
    }>();
    &()
}

fn main() {}


