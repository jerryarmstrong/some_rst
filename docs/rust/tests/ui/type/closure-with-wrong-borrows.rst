tests/ui/type/closure-with-wrong-borrows.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<'a>(&'a str);

fn f(inner: fn(&str, &S)) {
}

#[allow(unreachable_code)]
fn main() {
    let inner: fn(_, _) = unimplemented!();
    f(inner); //~ ERROR mismatched types
}


