tests/ui/privacy/privacy4.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(lang_items, start, no_core)]
#![no_core] // makes debugging this test *a lot* easier (during resolve)

#[lang = "sized"] pub trait Sized {}
#[lang="copy"] pub trait Copy {}

// Test to make sure that private items imported through globs remain private
// when  they're used.

mod bar {
    pub use self::glob::*;

    mod glob {
        fn gpriv() {}
    }
}

pub fn foo() {}

fn test2() {
    use bar::glob::gpriv; //~ ERROR: module `glob` is private
    gpriv();
}

#[start] fn main(_: isize, _: *const *const u8) -> isize { 3 }


