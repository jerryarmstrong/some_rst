tests/ui/imports/local-modularized-tricky-fail-2.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Crate-local macro expanded `macro_export` macros cannot be accessed with module-relative paths.

macro_rules! define_exported { () => {
    #[macro_export]
    macro_rules! exported {
        () => ()
    }
}}

define_exported!();

mod m {
    use exported;
    //~^ ERROR macro-expanded `macro_export` macros from the current crate cannot
    //~| WARN this was previously accepted
}

fn main() {
    ::exported!();
    //~^ ERROR macro-expanded `macro_export` macros from the current crate cannot
    //~| WARN this was previously accepted
}


