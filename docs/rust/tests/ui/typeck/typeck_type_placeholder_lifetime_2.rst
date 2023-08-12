tests/ui/typeck/typeck_type_placeholder_lifetime_2.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that the `_` type placeholder does not react
// badly if put as a lifetime parameter.

struct Foo<'a, T:'a> {
    r: &'a T
}

pub fn main() {
    let c: Foo<_, usize> = Foo { r: &5 };
    //~^ ERROR this struct takes 1 generic argument but 2 generic arguments were supplied
}


