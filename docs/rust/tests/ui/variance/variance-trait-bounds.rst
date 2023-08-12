tests/ui/variance/variance-trait-bounds.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![feature(rustc_attrs)]

// Check that bounds on type parameters (other than `Self`) do not
// influence variance.

trait Getter<T> {
    fn get(&self) -> T;
}

trait Setter<T> {
    fn get(&self, _: T);
}

#[rustc_variance]
struct TestStruct<U,T:Setter<U>> { //~ ERROR [+, +]
    t: T, u: U
}

#[rustc_variance]
enum TestEnum<U,T:Setter<U>> { //~ ERROR [*, +]
    Foo(T)
}

#[rustc_variance]
struct TestContraStruct<U,T:Setter<U>> { //~ ERROR [*, +]
    t: T
}

#[rustc_variance]
struct TestBox<U,T:Getter<U>+Setter<U>> { //~ ERROR [*, +]
    t: T
}

pub fn main() { }


