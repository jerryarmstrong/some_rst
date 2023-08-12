tests/rustdoc/edition-flag.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test
// edition:2018

/// ```rust
/// fn main() {
///     let _ = async { };
/// }
/// ```
fn main() {
    let _ = async { };
}


