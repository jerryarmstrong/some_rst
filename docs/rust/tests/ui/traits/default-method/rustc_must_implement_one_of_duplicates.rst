tests/ui/traits/default-method/rustc_must_implement_one_of_duplicates.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_must_implement_one_of(a, a)]
//~^ functions names are duplicated
trait Trait {
    fn a() {}
}

#[rustc_must_implement_one_of(b, a, a, c, b, c)]
//~^ functions names are duplicated
//~| functions names are duplicated
//~| functions names are duplicated
trait Trait1 {
    fn a() {}
    fn b() {}
    fn c() {}
}

fn main() {}


