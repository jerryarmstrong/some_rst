tests/ui/feature-gates/feature-gate-vectorcall.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-abi_vectorcall
// needs-llvm-components: x86
// compile-flags: --target=i686-pc-windows-msvc --crate-type=rlib
#![no_core]
#![feature(no_core, lang_items)]
#[lang="sized"]
trait Sized { }

// Test that the "vectorcall-unwind" ABI is feature-gated, and cannot be used when
// the `c_unwind` feature gate is not used.

extern "vectorcall" fn f() {} //~ ERROR vectorcall is experimental

trait T {
    extern "vectorcall" fn m(); //~ ERROR vectorcall is experimental

    extern "vectorcall" fn dm() {} //~ ERROR vectorcall is experimental
}

struct S;
impl T for S {
    extern "vectorcall" fn m() {} //~ ERROR vectorcall is experimental
}

impl S {
    extern "vectorcall" fn im() {} //~ ERROR vectorcall is experimental
}

type TA = extern "vectorcall" fn(); //~ ERROR vectorcall is experimental

extern "vectorcall" {} //~ ERROR vectorcall is experimental


