tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-2.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(&mut (ref mut v, w): &mut (&u8, &u8), x: &u8) {
    *v = x;
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


