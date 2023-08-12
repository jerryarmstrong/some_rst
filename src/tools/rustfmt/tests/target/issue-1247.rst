src/tools/rustfmt/tests/target/issue-1247.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-max_width: 80

fn foo() {
    polyfill::slice::fill(
        &mut self.pending[padding_pos..(self.algorithm.block_len - 8)],
        0,
    );
}


