tests/ui/parser/fn-defined-using-func.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check what happens when `func` is used to define a function, instead of `fn`
// edition:2021

#![allow(dead_code)]

func foo() {}
//~^ ERROR expected one of `!` or `::`, found `foo`
//~^^ HELP write `fn` instead of `func` to declare a function

fn main() {}


