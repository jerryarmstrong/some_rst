tests/ui/imports/local-modularized-tricky-fail-1.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

macro_rules! define_exported { () => {
    #[macro_export]
    macro_rules! exported {
        () => ()
    }
}}
macro_rules! define_panic { () => {
    #[macro_export]
    macro_rules! panic {
        () => ()
    }
}}
macro_rules! define_include { () => {
    #[macro_export]
    macro_rules! include {
        () => ()
    }
}}

use inner1::*;

mod inner1 {
    pub macro exported() {}
}

exported!(); //~ ERROR `exported` is ambiguous

mod inner2 {
    define_exported!();
}

fn main() {
    panic!(); //~ ERROR `panic` is ambiguous
}

mod inner3 {
    define_panic!();
}

mod inner4 {
    define_include!();
}

include!(); //~ ERROR `include` is ambiguous


