tests/ui/feature-gates/feature-gate-unboxed-closures.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(fn_traits)]

struct Test;

impl FnOnce<(u32, u32)> for Test {
//~^ ERROR the precise format of `Fn`-family traits' type parameters is subject to change
//~| ERROR manual implementations of `FnOnce` are experimental
    type Output = u32;

    extern "rust-call" fn call_once(self, (a, b): (u32, u32)) -> u32 {
        a + b
    }
    //~^^^ ERROR rust-call ABI is subject to change
}

fn main() {
    assert_eq!(Test(1u32, 2u32), 3u32);
}


