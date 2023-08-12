tests/ui/suggestions/bool_typo_err_suggest.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Suggest the boolean value instead of emit a generic error that the value
// True is not in the scope.

fn main() {
    let x = True;
    //~^ ERROR cannot find value `True` in this scope
    //~| HELP you may want to use a bool value instead

    let y = False;
    //~^ ERROR cannot find value `False` in this scope
    //~| HELP you may want to use a bool value instead
}


