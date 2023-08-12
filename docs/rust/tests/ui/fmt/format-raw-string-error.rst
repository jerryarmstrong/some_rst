tests/ui/fmt/format-raw-string-error.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!(r#"\'\'\'\'\'\'\'\'\'\'\'\'\'\'}"#); //~ ERROR invalid format string: unmatched `}` found
}


