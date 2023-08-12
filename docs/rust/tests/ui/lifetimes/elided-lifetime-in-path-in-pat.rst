tests/ui/lifetimes/elided-lifetime-in-path-in-pat.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Foo<'a> {
    x: &'a (),
}

// The lifetime in pattern-position `Foo` is elided.
// Verify that lowering does not create an independent lifetime parameter for it.
fn foo<'a>(Foo { x }: Foo<'a>) {
    *x
}

fn main() {}


