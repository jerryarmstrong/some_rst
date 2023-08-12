tests/ui/const-generics/generic_const_exprs/from-sig.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

struct Foo<const B: bool>;

fn test<const N: usize>() -> Foo<{ N > 10 }> {
    Foo
}

fn main() {
    let _: Foo<true> = test::<12>();
    let _: Foo<false> = test::<9>();
}


