tests/ui/incoherent-inherent-impls/no-attr-empty-impl.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:extern-crate.rs
extern crate extern_crate;

impl extern_crate::StructWithAttr {}
//~^ ERROR cannot define inherent `impl` for a type outside of the crate

impl extern_crate::StructNoAttr {}
//~^ ERROR cannot define inherent `impl` for a type outside of the crate

impl extern_crate::EnumWithAttr {}
//~^ ERROR cannot define inherent `impl` for a type outside of the crate

impl extern_crate::EnumNoAttr {}
//~^ ERROR cannot define inherent `impl` for a type outside of the crate

impl f32 {} //~ ERROR cannot define inherent `impl` for primitive types

fn main() {}


