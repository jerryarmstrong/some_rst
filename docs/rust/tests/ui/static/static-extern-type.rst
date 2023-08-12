tests/ui/static/static-extern-type.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![feature(extern_types)]

pub mod a {
    extern "C" {
        pub type StartFn;
        pub static start: StartFn;
    }
}

pub mod b {
    #[repr(transparent)]
    pub struct TransparentType(::a::StartFn);
    extern "C" {
        pub static start: TransparentType;
    }
}

pub mod c {
    #[repr(C)]
    pub struct CType(u32, ::b::TransparentType);
    extern "C" {
        pub static start: CType;
    }
}

fn main() {}


