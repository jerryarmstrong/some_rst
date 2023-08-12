tests/ui/abi/rustcall-generic.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: normal opt
// check-pass
//[opt] compile-flags: -Zmir-opt-level=3

#![feature(unboxed_closures, tuple_trait)]

extern "rust-call" fn foo<T: std::marker::Tuple>(_: T) {}

fn main() {
    foo(());
    foo((1, 2));
}


