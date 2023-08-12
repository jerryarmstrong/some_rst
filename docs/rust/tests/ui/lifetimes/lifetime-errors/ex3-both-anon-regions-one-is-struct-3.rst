tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-one-is-struct-3.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, 'b> { a: &'a u32, b: &'b u32 }

fn foo(mut y: Ref, x: &u32) {
    y.b = x;
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


