tests/ui/methods/method-call-lifetime-args-subst-index.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![allow(unused)]

struct S;

impl S {
    fn early_and_type<'a, T>(self) -> &'a T { loop {} }
}

fn test() {
    S.early_and_type::<u16>();
}


fn main() {}


