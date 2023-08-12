tests/ui/type-alias-impl-trait/generic_lifetime_param.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]

fn main() {}

type Region<'a> = impl std::fmt::Debug + 'a;


fn region<'b>(a: &'b ()) -> Region<'b> {
    a
}


