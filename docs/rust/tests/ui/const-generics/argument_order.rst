tests/ui/const-generics/argument_order.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bad<const N: usize, T> {
    arr: [u8; { N }],
    another: T,
}

struct AlsoBad<const N: usize, 'a, T, 'b, const M: usize, U> {
    //~^ ERROR lifetime parameters must be declared prior
    a: &'a T,
    b: &'b U,
}

fn main() {
    let _: AlsoBad<7, 'static, u32, 'static, 17, u16>;
    //~^ ERROR lifetime provided when a type was expected
 }


