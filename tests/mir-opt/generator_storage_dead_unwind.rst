tests/mir-opt/generator_storage_dead_unwind.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-wasm32-bare compiled with panic=abort by default

// Test that we generate StorageDead on unwind paths for generators.
//
// Basic block and local names can safely change, but the StorageDead statements
// should not go away.

#![feature(generators, generator_trait)]

struct Foo(i32);

impl Drop for Foo {
    fn drop(&mut self) {}
}

struct Bar(i32);

fn take<T>(_x: T) {}

// EMIT_MIR generator_storage_dead_unwind.main-{closure#0}.StateTransform.before.mir
fn main() {
    let _gen = || {
        let a = Foo(5);
        let b = Bar(6);
        yield;
        take(a);
        take(b);
    };
}


