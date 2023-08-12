tests/ui/parser/match-refactor-to-expr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let foo =
        match //~ NOTE while parsing this `match` expression
        Some(4).unwrap_or(5)
        //~^ NOTE expected one of `.`, `?`, `{`, or an operator
        ; //~ NOTE unexpected token
        //~^ ERROR expected one of `.`, `?`, `{`, or an operator, found `;`

    println!("{}", foo)
}


