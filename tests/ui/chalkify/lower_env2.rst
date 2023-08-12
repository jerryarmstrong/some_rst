tests/ui/chalkify/lower_env2.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

#![allow(dead_code)]

trait Foo { }

struct S<'a, T: ?Sized> where T: Foo {
    data: &'a T,
}

fn bar<T: Foo>(_x: S<'_, T>) { // note that we have an implicit `T: Sized` bound
}

fn main() {
}


