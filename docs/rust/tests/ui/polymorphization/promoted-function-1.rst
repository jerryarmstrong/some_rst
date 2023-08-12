tests/ui/polymorphization/promoted-function-1.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags: -Zpolymorphize=on
#![crate_type = "lib"]
#![feature(rustc_attrs)]

fn foo<'a>(_: &'a ()) {}

#[rustc_polymorphize_error]
pub fn test<T>() {
    //~^ ERROR item has unused generic parameters
    foo(&());
}


