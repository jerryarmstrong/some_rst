src/tools/rustfmt/tests/target/configs/indent_style/block_trailing_comma_call/two.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two
// rustfmt-error_on_line_overflow: false
// rustfmt-indent_style: Block

// rustfmt should not add trailing comma when rewriting macro. See #1528.
fn a() {
    panic!(
        "this is a long string that goes past the maximum line length causing rustfmt to insert a comma here:"
    );
    foo(
        a,
        oooptoptoptoptptooptoptoptoptptooptoptoptoptptoptoptoptoptpt(),
    );
}


