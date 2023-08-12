src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0034_crate_path_in_call.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    make_query(crate::module_map::module_tree);
}


