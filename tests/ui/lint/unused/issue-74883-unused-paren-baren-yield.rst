tests/ui/lint/unused/issue-74883-unused-paren-baren-yield.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generator_trait)]
#![feature(generators)]
#![deny(unused_braces, unused_parens)]

use std::ops::Generator;
use std::pin::Pin;

fn main() {
    let mut x = |_| {
        while let Some(_) = (yield) {}
        while let Some(_) = {yield} {}

        // Only warn these cases
        while let Some(_) = ({yield}) {} //~ ERROR: unnecessary parentheses
        while let Some(_) = ((yield)) {} //~ ERROR: unnecessary parentheses
        {{yield}}; //~ ERROR: unnecessary braces
        {( yield )}; //~ ERROR: unnecessary parentheses
        while let Some(_) = {(yield)} {} //~ ERROR: unnecessary parentheses
        while let Some(_) = {{yield}} {} //~ ERROR: unnecessary braces

        // FIXME: It'd be great if we could also warn them.
        ((yield));
        ({ yield });
    };
    let _ = Pin::new(&mut x).resume(Some(5));
}


