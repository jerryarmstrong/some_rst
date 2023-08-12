tests/ui/parser/recover-for-loop-parens-around-head.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Here we test that the parser is able to recover in a situation like
// `for ( $pat in $expr )` since that is familiar syntax in other languages.
// Instead we suggest that the user writes `for $pat in $expr`.

#![deny(unused)] // Make sure we don't trigger `unused_parens`.

fn main() {
    let vec = vec![1, 2, 3];

    for ( elem in vec ) {
        //~^ ERROR expected one of `)`, `,`, `@`, or `|`, found keyword `in`
        //~| ERROR unexpected parentheses surrounding `for` loop head
        const RECOVERY_WITNESS: () = 0; //~ ERROR mismatched types
    }
}


