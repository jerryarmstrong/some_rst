src/tools/rustfmt/tests/target/configs/format_strings/false.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: false
// rustfmt-max_width: 50
// rustfmt-error_on_line_overflow: false
// Force format strings

fn main() {
    let lorem = "ipsum dolor sit amet consectetur adipiscing elit lorem ipsum dolor sit";
}


