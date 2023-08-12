tests/ui/rust-2018/auxiliary/edition-lint-paths.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo() {}

#[macro_export]
macro_rules! macro_2015 {
    () => {
        use edition_lint_paths as other_name;
        use edition_lint_paths::foo as other_foo;
        fn check_macro_2015() {
            ::edition_lint_paths::foo();
        }
    }
}


