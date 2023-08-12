tests/ui/const-generics/defaults/wrong-order.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A<T = u32, const N: usize> {
    //~^ ERROR generic parameters with a default must be trailing
    arg: T,
}

struct Foo<const N: u8 = 3, T>(T);
//~^ error: generic parameters with a default must be trailing

fn main() {}


