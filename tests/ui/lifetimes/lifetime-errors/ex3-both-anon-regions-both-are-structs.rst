tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-both-are-structs.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a> {
    x: &'a u32,
}

fn foo(mut x: Vec<Ref>, y: Ref) {
    x.push(y);
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


