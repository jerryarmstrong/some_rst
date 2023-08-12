tests/ui/issues/issue-7970a.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! one_arg_macro {
    ($fmt:expr) => (print!(concat!($fmt, "\n")));
}

fn main() {
    one_arg_macro!();
    //~^ ERROR unexpected end of macro invocation
}


