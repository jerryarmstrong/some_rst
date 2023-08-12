tests/ui/macros/macro-missing-fragment.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(missing_fragment_specifier)]

macro_rules! used_arm {
    ( $( any_token $field_rust_type )* ) => {};
    //~^ ERROR missing fragment
    //~| WARN missing fragment
    //~| WARN this was previously accepted
}

macro_rules! used_macro_unused_arm {
    () => {};
    ( $name ) => {};
    //~^ WARN missing fragment
    //~| WARN this was previously accepted
}

macro_rules! unused_macro {
    ( $name ) => {};
    //~^ WARN missing fragment
    //~| WARN this was previously accepted
}

fn main() {
    used_arm!();
    used_macro_unused_arm!();
}


