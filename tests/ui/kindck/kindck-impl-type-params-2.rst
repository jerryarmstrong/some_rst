tests/ui/kindck/kindck-impl-type-params-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
}



impl<T:Copy> Foo for T {
}

fn take_param<T:Foo>(foo: &T) { }

fn main() {
    let x: Box<_> = Box::new(3);
    take_param(&x);
    //~^ ERROR the trait bound `Box<{integer}>: Copy` is not satisfied
}


