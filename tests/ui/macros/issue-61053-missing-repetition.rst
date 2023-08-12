tests/ui/macros/issue-61053-missing-repetition.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(meta_variable_misuse)]

macro_rules! foo {
    () => {};
    ($( $i:ident = $($j:ident),+ );*) => { $( $i = $j; )* };
    //~^ ERROR variable 'j' is still repeating
}

macro_rules! bar {
    () => {};
    (test) => {
        macro_rules! nested {
            () => {};
            ($( $i:ident = $($j:ident),+ );*) => { $( $i = $j; )* };
            //~^ ERROR variable 'j' is still repeating
        }
    };
    ( $( $i:ident = $($j:ident),+ );* ) => {
        $(macro_rules! $i {
            () => { $j }; //~ ERROR variable 'j' is still repeating
        })*
    };
}

fn main() {
    foo!();
    bar!();
}


