tests/ui/lint/opaque-ty-ffi-unsafe.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![deny(improper_ctypes)]

type A = impl Fn();

pub fn ret_closure() -> A {
    || {}
}

extern "C" {
    pub fn a(_: A);
    //~^ ERROR `extern` block uses type `A`, which is not FFI-safe [improper_ctypes]
}

fn main() {}


