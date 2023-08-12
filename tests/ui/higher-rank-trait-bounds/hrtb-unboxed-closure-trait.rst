tests/ui/higher-rank-trait-bounds/hrtb-unboxed-closure-trait.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test HRTB used with the `Fn` trait.

fn foo<F:Fn(&isize)>(f: F) {
    let x = 22;
    f(&x);
}

fn main() {
    foo(|x: &isize| println!("{}", *x));
}


