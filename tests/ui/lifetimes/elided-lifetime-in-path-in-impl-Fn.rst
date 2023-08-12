tests/ui/lifetimes/elided-lifetime-in-path-in-impl-Fn.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Foo<'a>(&'a ());

fn with_fn() -> fn(Foo) {
    |_| ()
}

fn with_impl_fn() -> impl Fn(Foo) {
    |_| ()
}

fn with_where_fn<T>()
where
    T: Fn(Foo),
{
}

fn main() {}


