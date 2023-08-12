tests/ui/pattern/issue-80186-mut-binding-help-suggestion.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for correct pretty-printing of an AST representing `&(mut x)` in help
// suggestion diagnostic.

fn main() {
    let mut &x = &0;
    //~^ ERROR `mut` must be attached to each individual binding
    //~| HELP add `mut` to each binding
    //~| SUGGESTION &(mut x)
}


