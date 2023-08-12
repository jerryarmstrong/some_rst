src/tools/rustfmt/tests/target/format_strings/issue-687.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true

fn foo() -> &'static str {
    let sql = "ATTACH DATABASE ':memory:' AS my_attached;
               BEGIN;
               CREATE TABLE my_attached.foo(x INTEGER);
               INSERT INTO my_attached.foo VALUES(42);
               END;";
    sql
}


