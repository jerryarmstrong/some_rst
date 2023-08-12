tests/ui/feature-gates/feature-gate-staged_api.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![stable(feature = "a", since = "b")]
//~^ ERROR stability attributes may not be used outside of the standard library
mod inner_private_module {
    // UnnameableTypeAlias isn't marked as reachable, so no stability annotation is required here
    pub type UnnameableTypeAlias = u8;
}

#[stable(feature = "a", since = "b")]
//~^ ERROR stability attributes may not be used outside of the standard library
pub fn f() -> inner_private_module::UnnameableTypeAlias {
    0
}

fn main() {}


