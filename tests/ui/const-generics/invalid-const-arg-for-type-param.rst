tests/ui/const-generics/invalid-const-arg-for-type-param.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::convert::TryInto;

struct S;

fn main() {
    let _: u32 = 5i32.try_into::<32>().unwrap();
    //~^ ERROR this associated function takes

    S.f::<0>();
    //~^ ERROR no method named `f`

    S::<0>;
    //~^ ERROR this struct takes 0
}


