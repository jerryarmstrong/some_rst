tests/codegen-units/item-collection/asm-sym.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// compile-flags: -Ccodegen-units=1 -Zprint-mono-items=lazy --crate-type=lib

#[inline(always)]
pub unsafe fn f() {
    //~ MONO_ITEM static f::S @@ asm_sym-cgu.0[External]
    static S: usize = 1;
    //~ MONO_ITEM fn f::fun @@ asm_sym-cgu.0[External]
    fn fun() {}
    core::arch::asm!("/* {0} {1} */", sym S, sym fun);
}

//~ MONO_ITEM fn g @@ asm_sym-cgu.0[External]
pub unsafe fn g() {
    //~ MONO_ITEM static g::S @@ asm_sym-cgu.0[Internal]
    static S: usize = 2;
    //~ MONO_ITEM fn g::fun @@ asm_sym-cgu.0[Internal]
    fn fun() {}
    core::arch::asm!("/* {0} {1} */", sym S, sym fun);
}


