tests/rustdoc/auxiliary/rustdoc-extern-method.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]
#![feature(unboxed_closures)]

pub trait Foo {
    extern "rust-call" fn foo(&self, _: ()) -> i32;
    extern "rust-call" fn foo_(&self, _: ()) -> i32 { 0 }
}


