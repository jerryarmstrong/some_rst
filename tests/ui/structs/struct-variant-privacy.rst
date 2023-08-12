tests/ui/structs/struct-variant-privacy.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    enum Bar {
        Baz { a: isize },
    }
}

fn f(b: foo::Bar) {
    //~^ ERROR enum `Bar` is private
    match b {
        foo::Bar::Baz { a: _a } => {} //~ ERROR enum `Bar` is private
    }
}

fn main() {}


