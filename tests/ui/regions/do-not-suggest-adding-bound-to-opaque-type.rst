tests/ui/regions/do-not-suggest-adding-bound-to-opaque-type.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait T {}

struct S<'a>(&'a ());

impl<'a> T for S<'a> {}

fn foo() -> impl T {
    let x = ();
    S(&x) //~ ERROR `x` does not live long enough
}

fn main() {}


