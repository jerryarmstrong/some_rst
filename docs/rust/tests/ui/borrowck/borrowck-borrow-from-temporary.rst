tests/ui/borrowck/borrowck-borrow-from-temporary.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test lifetimes are linked properly when we take reference
// to interior.

fn id<T>(x: T) -> T { x }

struct Foo(isize);

fn foo<'a>() -> &'a isize {
    let &Foo(ref x) = &id(Foo(3));
    x //~ ERROR cannot return value referencing temporary value
}

pub fn main() {
}


