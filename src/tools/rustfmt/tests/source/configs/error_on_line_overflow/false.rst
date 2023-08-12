src/tools/rustfmt/tests/source/configs/error_on_line_overflow/false.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-error_on_line_overflow: false
// Error on line overflow

fn main() {
    let lorem_ipsum_dolor_sit_amet_consectetur_adipiscing_elit_lorem_ipsum_dolor_sit_amet_consectetur_adipiscing_elit;
}


