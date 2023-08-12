tests/ui/non_modrs_mods/foors_mod.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
//
// ignore-test: not a test, used by non_modrs_mods.rs

pub mod inner_modrs_mod;
pub mod inner_foors_mod;
pub mod inline {
    #[path="somename.rs"]
    pub mod innie;
}


