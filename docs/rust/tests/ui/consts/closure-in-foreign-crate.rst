tests/ui/consts/closure-in-foreign-crate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:closure-in-foreign-crate.rs
// build-pass

extern crate closure_in_foreign_crate;

const _: () = closure_in_foreign_crate::test();

fn main() {}


