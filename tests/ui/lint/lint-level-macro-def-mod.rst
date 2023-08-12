tests/ui/lint/lint-level-macro-def-mod.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This checks that exported macros lint as part of their module of origin, not
// the root module.
//
// check-pass

//! Top level documentation
#![deny(missing_docs)]

#[allow(missing_docs)]
mod module {
    #[macro_export]
    macro_rules! hello {
        () => ()
    }
}

fn main() {}


