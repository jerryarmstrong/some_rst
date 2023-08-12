src/tools/rustfmt/tests/target/issue-3131.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match 3 {
        t if match t {
            _ => true,
        } => {}
        _ => {}
    }
}


