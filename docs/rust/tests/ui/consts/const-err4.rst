tests/ui/consts/const-err4.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // stderr-per-bitwidth
#[derive(Copy, Clone)]
union Foo {
    a: isize,
    b: (),
}

enum Bar {
    Boo = [unsafe { Foo { b: () }.a }; 4][3],
    //~^ ERROR evaluation of constant value failed
    //~| uninitialized
}

fn main() {
    assert_ne!(Bar::Boo as isize, 0);
}


