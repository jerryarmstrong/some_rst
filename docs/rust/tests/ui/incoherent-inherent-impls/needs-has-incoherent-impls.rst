tests/ui/incoherent-inherent-impls/needs-has-incoherent-impls.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:extern-crate.rs
#![feature(rustc_attrs)]
extern crate extern_crate;

impl extern_crate::StructWithAttr {
    //~^ ERROR cannot define inherent `impl` for a type outside of the crate
    fn foo() {}
}
impl extern_crate::StructWithAttr {
    #[rustc_allow_incoherent_impl]
    fn bar() {}
}
impl extern_crate::StructNoAttr {
    //~^ ERROR cannot define inherent `impl` for a type outside of the crate
    fn foo() {}
}
impl extern_crate::StructNoAttr {
    //~^ ERROR cannot define inherent `impl` for a type outside of the crate
    #[rustc_allow_incoherent_impl]
    fn bar() {}
}
impl extern_crate::EnumWithAttr {
    //~^ ERROR cannot define inherent `impl` for a type outside of the crate
    fn foo() {}
}
impl extern_crate::EnumWithAttr {
    #[rustc_allow_incoherent_impl]
    fn bar() {}
}
impl extern_crate::EnumNoAttr {
    //~^ ERROR cannot define inherent `impl` for a type outside of the crate
    fn foo() {}
}
impl extern_crate::EnumNoAttr {
    //~^ ERROR cannot define inherent `impl` for a type outside of the crate
    #[rustc_allow_incoherent_impl]
    fn bar() {}
}

fn main() {}


