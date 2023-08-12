tests/rustdoc/intra-doc/cross-crate/auxiliary/module.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "module_inner"]
#![deny(rustdoc::broken_intra_doc_links)]
/// [SomeType] links to [bar]
pub struct SomeType;
pub trait SomeTrait {}
/// [bar] links to [SomeTrait] and also [SomeType]
pub mod bar {}


