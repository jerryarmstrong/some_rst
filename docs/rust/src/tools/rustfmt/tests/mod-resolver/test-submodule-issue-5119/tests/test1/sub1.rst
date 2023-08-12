src/tools/rustfmt/tests/mod-resolver/test-submodule-issue-5119/tests/test1/sub1.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustfmt_test_submodule_issue::foo;

#[test]
fn test_foo() {
assert_eq!(3, foo());
}


