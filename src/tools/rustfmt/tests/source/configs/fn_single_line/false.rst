src/tools/rustfmt/tests/source/configs/fn_single_line/false.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-fn_single_line: false
// Single-expression function on single line

fn lorem() -> usize {
    42
}

fn lorem() -> usize {
    let ipsum = 42;
    ipsum
}


