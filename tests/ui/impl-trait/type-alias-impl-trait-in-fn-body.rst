tests/ui/impl-trait/type-alias-impl-trait-in-fn-body.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![feature(type_alias_impl_trait)]

use std::fmt::Debug;

fn main() {
    type Existential = impl Debug;

    fn f() -> Existential {}
    println!("{:?}", f());
}


