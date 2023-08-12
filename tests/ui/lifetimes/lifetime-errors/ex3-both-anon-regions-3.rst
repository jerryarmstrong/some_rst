tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-3.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(z: &mut Vec<(&u8,&u8)>, (x, y): (&u8, &u8)) {
    z.push((x,y));
    //~^ ERROR lifetime may not live long enough
    //~| ERROR lifetime may not live long enough
}

fn main() { }


