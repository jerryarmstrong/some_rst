tests/codegen-units/item-collection/static-init.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Zprint-mono-items=eager -Zpolymorphize=on

#![feature(start)]

pub static FN : fn() = foo::<i32>;

pub fn foo<T>() { }

//~ MONO_ITEM fn foo::<T>
//~ MONO_ITEM static FN

//~ MONO_ITEM fn start
#[start]
fn start(_: isize, _: *const *const u8) -> isize {
    0
}


