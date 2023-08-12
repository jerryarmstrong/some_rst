tests/ui/associated-consts/associated-const-dead-code.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(dead_code)]

struct MyFoo;

impl MyFoo {
    const BAR: u32 = 1;
    //~^ ERROR associated constant `BAR` is never used
}

fn main() {
    let _: MyFoo = MyFoo;
}


