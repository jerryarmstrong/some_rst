tests/ui/dyn-keyword/dyn-2015-no-warnings-without-lints.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Under the 2015 edition without the keyword_idents lint, `dyn` is
// entirely acceptable as an identifier.
//
// check-pass
// edition:2015

#![allow(non_camel_case_types)]

mod outer_mod {
    pub mod dyn {
        pub struct dyn;
    }
}
use outer_mod::dyn::dyn;

fn main() {
    match dyn { dyn => {} }
    macro_defn::dyn();
}
mod macro_defn {
    macro_rules! dyn {
        () => { ::outer_mod::dyn::dyn }
    }

    pub fn dyn() -> ::outer_mod::dyn::dyn {
        dyn!()
    }
}


