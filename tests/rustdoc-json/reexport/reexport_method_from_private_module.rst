tests/rustdoc-json/reexport/reexport_method_from_private_module.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/102583>.

// @set impl_S = "$.index[*][?(@.docs=='impl S')].id"
// @has "$.index[*][?(@.name=='S')].inner.impls[*]" $impl_S
// @set is_present = "$.index[*][?(@.name=='is_present')].id"
// @is "$.index[*][?(@.docs=='impl S')].inner.items[*]" $is_present
// @!has "$.index[*][?(@.name=='hidden_impl')]"
// @!has "$.index[*][?(@.name=='hidden_fn')]"

#![no_std]

mod private_mod {
    pub struct S;

    /// impl S
    impl S {
        pub fn is_present() {}
        #[doc(hidden)]
        pub fn hidden_fn() {}
    }

    #[doc(hidden)]
    impl S {
        pub fn hidden_impl() {}
    }
}

pub use private_mod::*;


