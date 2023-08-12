tests/ui/macros/stmt_expr_attr_macro_parse.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_macro_rules)]

macro_rules! m {
    ($e:expr) => {
        "expr includes attr"
    };
    (#[$attr:meta] $e:expr) => {
        "expr excludes attr"
    }
}

macro_rules! n {
    (#[$attr:meta] $e:expr) => {
        "expr excludes attr"
    };
    ($e:expr) => {
        "expr includes attr"
    }
}

fn main() {
    assert_eq!(m!(#[attr] 1), "expr includes attr");
    assert_eq!(n!(#[attr] 1), "expr excludes attr");
}


