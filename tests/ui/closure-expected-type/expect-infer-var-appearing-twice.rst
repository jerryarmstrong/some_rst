tests/ui/closure-expected-type/expect-infer-var-appearing-twice.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn with_closure<F, A>(_: F)
    where F: FnOnce(A, A)
{
}

fn a() {
    with_closure(|x: u32, y| {
        // We deduce type of `y` from `x`.
    });
}

fn b() {
    // Here we take the supplied types, resulting in an error later on.
    with_closure(|x: u32, y: i32| {
        //~^ ERROR type mismatch in closure arguments
    });
}

fn c() {
    with_closure(|x, y: i32| {
        // We deduce type of `x` from `y`.
    });
}

fn main() { }


