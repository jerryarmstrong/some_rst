tests/ui/infinite/infinite-struct.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Take(Take);
//~^ ERROR has infinite size

// check that we don't hang trying to find the tail of a recursive struct (#79437)
fn foo() -> Take {
    Take(loop {})
}

// mutually infinite structs
struct Foo { //~ ERROR has infinite size
    x: Bar<Foo>,
}

struct Bar<T>([T; 1]);

fn main() {}


