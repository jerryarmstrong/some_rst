tests/ui/empty/empty-comment.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `/**/` was previously regarded as a doc comment because it starts with `/**` and ends with `*/`.
// This could break some internal logic that assumes the length of a doc comment is at least 5,
// leading to an ICE.

macro_rules! one_arg_macro {
    ($fmt:expr) => (print!(concat!($fmt, "\n")));
}

fn main() {
    one_arg_macro!(/**/); //~ ERROR unexpected end
}


