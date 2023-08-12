src/tools/rustfmt/tests/target/issue-3055/backtick.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: true

/// Simple block
///
/// ```text
///  `
/// ```
fn main() {
    println!("Hello, world!");
}


