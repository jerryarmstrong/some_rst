src/tools/rustfmt/tests/target/issue_3937.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_code_in_doc_comments:true

struct Foo {
    // a: i32,
    //
    // b: i32,
}

struct Foo {
    a: i32,
    //
    // b: i32,
}


