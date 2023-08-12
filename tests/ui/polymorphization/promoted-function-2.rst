tests/ui/polymorphization/promoted-function-2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags:-Zpolymorphize=on
#![crate_type = "lib"]
#![feature(generic_const_exprs, rustc_attrs)]
//~^ WARN the feature `generic_const_exprs` is incomplete

#[rustc_polymorphize_error]
fn test<T>() {
    //~^ ERROR item has unused generic parameters
    let x = [0; 3 + 4];
}

pub fn caller() {
    test::<String>();
    test::<Vec<String>>();
}


