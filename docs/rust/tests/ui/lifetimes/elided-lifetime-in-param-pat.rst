tests/ui/lifetimes/elided-lifetime-in-param-pat.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct S<T> {
    _t: T,
}

fn f(S::<&i8> { .. }: S<&i8>) {}

fn main() {
    f(S { _t: &42_i8 });
}


