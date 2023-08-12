tests/ui/associated-item/associated-item-duplicate-bounds.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Adapter {
    const LINKS: usize;
}

struct Foo<A: Adapter> {
    adapter: A,
    links: [u32; A::LINKS], // Shouldn't suggest bounds already there.
    //~^ ERROR generic parameters may not be used in const operations
}

fn main() {}


