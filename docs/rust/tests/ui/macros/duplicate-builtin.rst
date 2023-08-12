tests/ui/macros/duplicate-builtin.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--crate-type lib
#![feature(decl_macro)]
#![feature(rustc_attrs)]

#[rustc_builtin_macro]
pub macro test($item:item) {
//~^ NOTE previously defined
    /* compiler built-in */
}

mod inner {
    #[rustc_builtin_macro]
    pub macro test($item:item) {
    //~^ ERROR attempted to define built-in macro more than once [E0773]
        /* compiler built-in */
    }
}


