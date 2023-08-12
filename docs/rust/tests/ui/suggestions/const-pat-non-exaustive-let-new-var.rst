tests/ui/suggestions/const-pat-non-exaustive-let-new-var.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let A = 3;
    //~^ ERROR refutable pattern in local binding
    //~| patterns `i32::MIN..=1_i32` and `3_i32..=i32::MAX` not covered
    //~| missing patterns are not covered because `a` is interpreted as a constant pattern, not a new variable
    //~| HELP introduce a variable instead
    //~| SUGGESTION a_var

    const A: i32 = 2;
    //~^ constant defined here
}


