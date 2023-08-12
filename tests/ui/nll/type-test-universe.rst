tests/ui/nll/type-test-universe.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #98095: make sure that
// we detect that S needs to outlive 'static.

fn outlives_forall<T>()
where
    for<'u> T: 'u,
{
}

fn test1<S>() {
    outlives_forall::<S>();
    //~^ ERROR `S` does not live long enough
}

struct Value<'a>(&'a ());
fn test2<'a>() {
    outlives_forall::<Value<'a>>();
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


