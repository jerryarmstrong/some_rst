tests/ui/unboxed-closures/unboxed-closure-sugar-used-on-struct.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that parentheses form doesn't work with struct types appearing in argument types.

struct Bar<A> {
    f: A
}

fn foo(b: Box<Bar()>) {
    //~^ ERROR parenthesized type parameters may only be used with a `Fn` trait
    //~| ERROR this struct takes 1 generic argument but 0 generic arguments
}

fn main() { }


