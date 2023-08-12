src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0059_loops_in_parens.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    Some(for _ in [1].into_iter() {});
    Some(loop { break; });
    Some(while true {});
}


