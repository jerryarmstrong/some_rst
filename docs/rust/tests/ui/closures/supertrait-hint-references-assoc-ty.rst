tests/ui/closures/supertrait-hint-references-assoc-ty.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub trait Fn0: Fn(i32) -> Self::Out {
    type Out;
}

impl<F: Fn(i32) -> ()> Fn0 for F {
    type Out = ();
}

pub fn closure_typer(_: impl Fn0) {}

fn main() {
    closure_typer(move |x| {
        let _: i64 = x.into();
    });
}


