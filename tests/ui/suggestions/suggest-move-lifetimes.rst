tests/ui/suggestions/suggest-move-lifetimes.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A<T, 'a> { //~ ERROR lifetime parameters must be declared
    t: &'a T,
}

struct B<T, 'a, U> { //~ ERROR lifetime parameters must be declared
    t: &'a T,
    u: U,
}

struct C<T, U, 'a> { //~ ERROR lifetime parameters must be declared
    t: &'a T,
    u: U,
}

struct D<T, U, 'a, 'b, V, 'c> { //~ ERROR lifetime parameters must be declared
    t: &'a T,
    u: &'b U,
    v: &'c V,
}

fn main() {}


