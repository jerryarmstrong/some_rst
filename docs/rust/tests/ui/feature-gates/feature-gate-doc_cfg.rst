tests/ui/feature-gates/feature-gate-doc_cfg.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc(cfg(unix))] //~ ERROR: `#[doc(cfg)]` is experimental
fn main() {}


