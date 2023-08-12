tests/ui/cross/cross-crate-macro-backtrace/auxiliary/extern_macro_crate.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]

pub fn print(_args: std::fmt::Arguments) {}

#[macro_export]
macro_rules! myprint {
    ($($arg:tt)*) => ($crate::print(format_args!($($arg)*)));
}

#[macro_export]
macro_rules! myprintln {
    ($fmt:expr) => (myprint!(concat!($fmt, "\n")));
}


