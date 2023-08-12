src/tools/rustfmt/tests/target/issue-5066/multi_line_struct_with_trailing_comma_always.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-trailing_comma: Always
// rustfmt-struct_lit_single_line: false

// There is an issue with how this is formatted.
// formatting should look like ./multi_line_struct_trailing_comma_always_struct_lit_width_0.rs
fn main() {
    let Foo {
        a, ..
    } = b;
}


