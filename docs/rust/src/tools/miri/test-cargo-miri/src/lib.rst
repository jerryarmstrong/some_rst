src/tools/miri/test-cargo-miri/src/lib.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// Doc-test test
/// ```rust
/// assert!(cargo_miri_test::make_true());
/// ```
/// ```rust,no_run
/// assert!(!cargo_miri_test::make_true());
/// ```
/// ```rust,compile_fail
/// assert!(cargo_miri_test::make_true() == 5);
/// ```
#[no_mangle]
pub fn make_true() -> bool {
    issue_1567::use_the_dependency();
    issue_1705::use_the_dependency();
    issue_1760::use_the_dependency!();
    issue_1691::use_me()
}

/// ```rust
/// cargo_miri_test::miri_only_fn();
/// ```
#[cfg(miri)]
pub fn miri_only_fn() {}

pub fn main() {
    println!("imported main");
}


