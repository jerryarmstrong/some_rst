tests/ui/consts/miri_unleashed/non_const_fn.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you

// A test demonstrating that we prevent calling non-const fn during CTFE.

fn foo() {}

static C: () = foo();
//~^ ERROR could not evaluate static initializer
//~| NOTE calling non-const function `foo`

fn main() {}


