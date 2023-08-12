tests/ui/parser/issues/issue-65257-invalid-var-decl-recovery.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    auto n = 0;//~ ERROR invalid variable declaration
    //~^ HELP write `let` instead of `auto` to introduce a new variable
    auto m;//~ ERROR invalid variable declaration
    //~^ HELP write `let` instead of `auto` to introduce a new variable
    m = 0;

    var n = 0;//~ ERROR invalid variable declaration
    //~^ HELP write `let` instead of `var` to introduce a new variable
    var m;//~ ERROR invalid variable declaration
    //~^ HELP write `let` instead of `var` to introduce a new variable
    m = 0;

    mut n = 0;//~ ERROR invalid variable declaration
    //~^ HELP missing keyword
    mut var;//~ ERROR invalid variable declaration
    //~^ HELP missing keyword
    var = 0;

    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


