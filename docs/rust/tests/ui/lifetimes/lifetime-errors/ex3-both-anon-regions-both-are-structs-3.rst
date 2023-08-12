tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-both-are-structs-3.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, 'b> {
    a: &'a u32,
    b: &'b u32,
}

fn foo(mut x: Ref) {
    x.a = x.b;
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


