src/tools/rust-analyzer/crates/parser/test_data/parser/err/0008_item_block_recovery.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
}

bar() {
    if true {
        1
    } else {
        2 + 3
    }
}

fn baz() {
}


