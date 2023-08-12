tests/ui/chalkify/generic_impls.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z trait-solver=chalk

trait Foo { }

impl<T> Foo for (T, u32) { }

fn gimme<F: Foo>() { }

fn foo<T>() {
    gimme::<(T, u32)>();
    gimme::<(Option<T>, u32)>();
    gimme::<(Option<T>, f32)>(); //~ ERROR
}

fn main() {
    gimme::<(i32, u32)>();
    gimme::<(i32, f32)>(); //~ ERROR
}


