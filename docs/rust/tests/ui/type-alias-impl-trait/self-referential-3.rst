tests/ui/type-alias-impl-trait/self-referential-3.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(type_alias_impl_trait)]

type Bar<'a, 'b> = impl PartialEq<Bar<'a, 'b>> + std::fmt::Debug;

fn bar<'a, 'b>(i: &'a i32) -> Bar<'a, 'b> {
    i
}

fn main() {
    let meh = 42;
    let muh = 42;
    assert_eq!(bar(&meh), bar(&muh));
}


