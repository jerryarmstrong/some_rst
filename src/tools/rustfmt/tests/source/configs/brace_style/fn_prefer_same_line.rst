src/tools/rustfmt/tests/source/configs/brace_style/fn_prefer_same_line.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: PreferSameLine
// Function brace style

fn lorem() {
    // body
}

fn lorem(ipsum: usize) {
    // body
}

fn lorem<T>(ipsum: T) where T: Add + Sub + Mul + Div {
    // body
}


