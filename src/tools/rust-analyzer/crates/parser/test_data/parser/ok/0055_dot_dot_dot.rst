src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0055_dot_dot_dot.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type X = ();

fn main() {
    let ():::X = ();
}


