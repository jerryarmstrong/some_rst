tests/run-make/raw-dylib-alt-calling-convention/driver.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate raw_dylib_alt_calling_convention_test;

fn main() {
    raw_dylib_alt_calling_convention_test::library_function(
        std::env::args().skip(1).next().map_or(
            false,
            |s| std::str::FromStr::from_str(&s).unwrap()));
}


