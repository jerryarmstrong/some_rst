tests/ui/consts/const-blocks/trait-error.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Copy, Clone)]
struct Foo<T>(T);

fn main() {
    [Foo(String::new()); 4];
    //~^ ERROR the trait bound `String: Copy` is not satisfied [E0277]
}


