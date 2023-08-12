tests/rustdoc/macro-indirect-use.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that it is possible to make a macro public through a `pub use` of its
// parent module.
//
// This is a regression test for issue #87257.

#![feature(decl_macro)]

mod outer {
    pub mod inner {
        pub macro some_macro() {}
    }
}

// @has macro_indirect_use/inner/index.html
// @has macro_indirect_use/inner/macro.some_macro.html
pub use outer::inner;


