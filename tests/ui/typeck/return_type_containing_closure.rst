tests/ui/typeck/return_type_containing_closure.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(unused)]
fn foo() { //~ HELP a return type might be missing here
    vec!['a'].iter().map(|c| c)
    //~^ ERROR mismatched types [E0308]
    //~| NOTE expected `()`, found struct `Map`
    //~| NOTE expected unit type `()`
    //~| HELP consider using a semicolon here
}

fn main() {}


