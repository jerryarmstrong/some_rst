tests/ui/privacy/priv-impl-prim-ty.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:priv-impl-prim-ty.rs

// pretty-expanded FIXME #23616

extern crate priv_impl_prim_ty as bar;

pub fn main() {
    bar::frob(1);

}


