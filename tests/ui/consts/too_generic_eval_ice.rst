tests/ui/consts/too_generic_eval_ice.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo<A, B>(A, B);

impl<A, B> Foo<A, B> {
    const HOST_SIZE: usize = std::mem::size_of::<B>();

    pub fn crash() -> bool {
        [5; Self::HOST_SIZE] == [6; 0]
        //~^ ERROR constant expression depends on a generic parameter
        //~| ERROR constant expression depends on a generic parameter
        //~| ERROR can't compare `[{integer}; Self::HOST_SIZE]` with `[{integer}; 0]`
    }
}

fn main() {}


