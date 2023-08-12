tests/ui/hygiene/auxiliary/transparent-basic.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro, rustc_attrs)]

#[rustc_macro_transparency = "transparent"]
pub macro dollar_crate() {
    let s = $crate::S;
}


