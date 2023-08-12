src/tools/rustfmt/tests/target/issue-5066/multi_line_struct_trailing_comma_never_struct_lit_width_0.rs
======================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-trailing_comma: Never
// rustfmt-struct_lit_single_line: false
// rustfmt-struct_lit_width: 0

fn main() {
    let Foo {
        a,
        ..
    } = b;
}


