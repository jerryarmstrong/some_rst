src/tools/rustfmt/tests/target/issue-3055/empty-code-block.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: true

/// Simple block
///
/// ```
/// ```
///
/// ```no_run
/// ```
///
/// ```should_panic
/// ```
///
/// ```compile_fail
/// ```
fn main() {
    println!("Hello, world!");
}


