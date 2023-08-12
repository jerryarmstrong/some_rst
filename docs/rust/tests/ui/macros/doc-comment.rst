tests/ui/macros/doc-comment.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Tests that we properly handle a nested macro expansion
// involving a `#[doc]` attribute
#![deny(missing_docs)]
//! Crate docs

macro_rules! doc_comment {
    ($x:expr, $($tt:tt)*) => {
        #[doc = $x]
        $($tt)*
    }
}

macro_rules! make_comment {
    () => {
        doc_comment!("Function docs",
            pub fn bar() {}
        );
    }
}


make_comment!();

fn main() {}


