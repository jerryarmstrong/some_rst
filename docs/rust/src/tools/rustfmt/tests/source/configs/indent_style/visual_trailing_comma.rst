src/tools/rustfmt/tests/source/configs/indent_style/visual_trailing_comma.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-error_on_line_overflow: false
// rustfmt-indent_style: Visual

// rustfmt should not add trailing comma when rewriting macro. See #1528.
fn a() {
    panic!("this is a long string that goes past the maximum line length causing rustfmt to insert a comma here:");
}


