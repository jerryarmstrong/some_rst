tests/ui/suggestions/suggest-assoc-fn-call-deref.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused)]

struct Foo<T>(T);

impl<T> Foo<T> {
    fn test() -> i32 { 1 }
}

fn main() {
    let x = Box::new(Foo(1i32));
    x.test();
    //~^ ERROR no method named `test` found for struct `Box<Foo<i32>>` in the current scope
}


