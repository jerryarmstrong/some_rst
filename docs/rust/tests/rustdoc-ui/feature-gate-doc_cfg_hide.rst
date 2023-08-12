tests/rustdoc-ui/feature-gate-doc_cfg_hide.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![doc(cfg_hide(test))]
//~^ ERROR `#[doc(cfg_hide)]` is experimental

#[cfg(not(test))]
pub fn public_fn() {}
#[cfg(test)]
pub fn internal_use_only() {}


