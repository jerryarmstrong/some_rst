tests/ui/incoherent-inherent-impls/auxiliary/extern-crate.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_has_incoherent_inherent_impls]
pub struct StructWithAttr;
pub struct StructNoAttr;

#[rustc_has_incoherent_inherent_impls]
pub enum EnumWithAttr {}
pub enum EnumNoAttr {}


