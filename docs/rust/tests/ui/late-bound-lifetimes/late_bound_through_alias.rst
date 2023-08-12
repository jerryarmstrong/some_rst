tests/ui/late-bound-lifetimes/late_bound_through_alias.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn f(_: X) -> X {
    unimplemented!()
}

fn g<'a>(_: X<'a>) -> X<'a> {
    unimplemented!()
}

type X<'a> = &'a ();

fn main() {
    let _: for<'a> fn(X<'a>) -> X<'a> = g;
    let _: for<'a> fn(X<'a>) -> X<'a> = f;
}


