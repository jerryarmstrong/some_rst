tests/ui/associated-consts/associated-const-type-parameter-arrays-2.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Foo {
    const Y: usize;
}

struct Abc;
impl Foo for Abc {
    const Y: usize = 8;
}

struct Def;
impl Foo for Def {
    const Y: usize = 33;
}

pub fn test<A: Foo, B: Foo>() {
    let _array = [4; <A as Foo>::Y];
    //~^ ERROR constant expression depends on a generic parameter
}

fn main() {
}


