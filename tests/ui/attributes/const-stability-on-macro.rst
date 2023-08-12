tests/ui/attributes/const-stability-on-macro.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "rust1", since = "1.0.0")]

#[rustc_const_stable(feature = "foo", since = "0")]
//~^ ERROR macros cannot have const stability attributes
macro_rules! foo {
    () => {};
}

#[rustc_const_unstable(feature = "bar", issue="none")]
//~^ ERROR macros cannot have const stability attributes
macro_rules! bar {
    () => {};
}

fn main() {}


