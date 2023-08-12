tests/ui/macros/issue-61053-unbound.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(meta_variable_misuse)]

macro_rules! foo {
    () => {};
    ($( $i:ident = $($j:ident),+ );*) => { $( $( $i = $k; )+ )* };
    //~^ ERROR unknown macro variable
}

macro_rules! bar {
    () => {};
    (test) => {
        macro_rules! nested {
            () => {};
            ($( $i:ident = $($j:ident),+ );*) => { $( $( $i = $k; )+ )* };
            //~^ ERROR unknown macro variable
        }
    };
    ( $( $i:ident = $($j:ident),+ );* ) => {
        $(macro_rules! $i {
            () => { $( $i = $k)+ }; //~ ERROR unknown macro variable
        })*
    };
}

fn main() {
    foo!();
    bar!();
}


