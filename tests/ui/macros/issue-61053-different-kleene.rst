tests/ui/macros/issue-61053-different-kleene.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(meta_variable_misuse)]

macro_rules! foo {
    () => {};
    ( $( $i:ident = $($j:ident),+ );* ) => { $( $( $i = $j; )* )* };
    //~^ ERROR meta-variable repeats with
    ( $( $($j:ident),+ );* ) => { $( $( $j; )+ )+ }; //~ERROR meta-variable repeats with
}

macro_rules! bar {
    () => {};
    (test) => {
        macro_rules! nested {
            () => {};
            ( $( $i:ident = $($j:ident),+ );* ) => { $( $( $i = $j; )* )* };
            //~^ ERROR meta-variable repeats with
            ( $( $($j:ident),+ );* ) => { $( $( $j; )+ )+ }; //~ERROR meta-variable repeats with
        }
    };
    ( $( $i:ident = $($j:ident),+ );* ) => {
        $(macro_rules! $i {
            () => { 0 $( + $j )* }; //~ ERROR meta-variable repeats with
        })*
    };
}

fn main() {
    foo!();
    bar!();
}


