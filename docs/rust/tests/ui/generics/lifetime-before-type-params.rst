tests/ui/generics/lifetime-before-type-params.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]
fn first<T, 'a, 'b>() {}
//~^ ERROR lifetime parameters must be declared prior to type and const parameters
fn second<'a, T, 'b>() {}
//~^ ERROR lifetime parameters must be declared prior to type and const parameters
fn third<T, U, 'a>() {}
//~^ ERROR lifetime parameters must be declared prior to type and const parameters
fn fourth<'a, T, 'b, U, 'c, V>() {}
//~^ ERROR lifetime parameters must be declared prior to type and const parameters

fn main() {}


