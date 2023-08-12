tests/ui/macros/issue-84632-eager-expansion-recursion-limit.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #84632: Recursion limit is ignored
// for builtin macros that eagerly expands.

#![recursion_limit = "15"]
macro_rules! a {
    () => ("");
    (A) => (concat!("", a!()));
    (A, $($A:ident),*) => (concat!("", a!($($A),*)))
    //~^ ERROR recursion limit reached
    //~| HELP consider increasing the recursion limit
}

fn main() {
    a!(A, A, A, A, A);
    a!(A, A, A, A, A, A, A, A, A, A, A);
}


