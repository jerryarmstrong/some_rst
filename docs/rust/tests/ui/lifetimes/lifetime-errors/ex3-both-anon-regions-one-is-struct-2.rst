tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-one-is-struct-2.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, 'b> { a: &'a u32, b: &'b u32 }

fn foo(mut x: Ref, y: &u32) {
    y = x.b;
    //~^ ERROR lifetime may not live long enough
    //~| ERROR cannot assign to immutable argument
}

fn main() { }


