tests/ui/editions/edition-keywords-2018-2015-expansion.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// aux-build:edition-kw-macro-2015.rs
// check-pass

#![allow(keyword_idents)]

#[macro_use]
extern crate edition_kw_macro_2015;

mod one_async {
    produces_async! {} // OK
}
mod two_async {
    produces_async_raw! {} // OK
}

fn main() {}


