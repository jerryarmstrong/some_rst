tests/run-make-fulldeps/save-analysis-rfc2126/extern_absolute_paths.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use krate2::hello;

fn main() {
    hello();
    ::krate2::hello();
}


