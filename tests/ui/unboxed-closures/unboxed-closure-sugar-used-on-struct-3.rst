tests/ui/unboxed-closures/unboxed-closure-sugar-used-on-struct-3.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that parentheses form parses in expression paths.

struct Bar<A,R> {
    f: A, r: R
}

impl<A,B> Bar<A,B> {
    fn new() -> Bar<A,B> { panic!() }
}

fn bar() {
    let b = Bar::<isize, usize>::new(); // OK

    let b = Bar::(isize, usize)::new(); // OK too (for the parser)
    //~^ ERROR parenthesized type parameters may only be used with a `Fn` trait
}

fn main() {}


