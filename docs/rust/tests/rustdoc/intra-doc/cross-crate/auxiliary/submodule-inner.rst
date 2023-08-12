tests/rustdoc/intra-doc/cross-crate/auxiliary/submodule-inner.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "a"]
#![deny(rustdoc::broken_intra_doc_links)]

pub mod bar {
   pub struct Bar;
}

pub mod foo {
  use crate::bar;
  /// link to [bar::Bar]
  pub struct Foo;
}


