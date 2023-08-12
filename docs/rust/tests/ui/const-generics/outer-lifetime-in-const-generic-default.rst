tests/ui/const-generics/outer-lifetime-in-const-generic-default.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<
    'a,
    const N: usize = {
        let x: &'a ();
        //~^ ERROR use of non-static lifetime `'a` in const generic
        3
    },
>(&'a ());

fn main() {}


