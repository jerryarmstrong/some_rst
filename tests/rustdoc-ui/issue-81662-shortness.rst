tests/rustdoc-ui/issue-81662-shortness.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test --error-format=short
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"
// failure-status: 101

/// ```rust
/// foo();
/// ```
//~^^ ERROR cannot find function `foo` in this scope
fn foo() {
    println!("Hello, world!");
}


