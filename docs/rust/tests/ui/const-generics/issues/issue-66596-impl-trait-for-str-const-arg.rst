tests/ui/const-generics/issues/issue-66596-impl-trait-for-str-const-arg.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(adt_const_params)]
#![allow(incomplete_features)]


trait Trait<const NAME: &'static str> {
    type Assoc;
}

impl Trait<"0"> for () {
    type Assoc = ();
}

fn main() {
    let _: <() as Trait<"0">>::Assoc = ();
}


