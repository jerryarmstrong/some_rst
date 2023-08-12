tests/ui/reachable-unnameable-type-alias.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(staged_api)]
#![stable(feature = "a", since = "b")]

mod inner_private_module {
    // UnnameableTypeAlias isn't marked as reachable, so no stability annotation is required here
    pub type UnnameableTypeAlias = u8;
}

#[stable(feature = "a", since = "b")]
pub fn f() -> inner_private_module::UnnameableTypeAlias {
    0
}

fn main() {}


