tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-latebound-regions.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<'a,'b>(x: &mut Vec<&'a u8>, y: &'b u8) {
    x.push(y);
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


