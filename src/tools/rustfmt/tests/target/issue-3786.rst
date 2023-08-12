src/tools/rustfmt/tests/target/issue-3786.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = r#"
this is a very long string exceeded maximum width in this case maximum 100. (current this line width is about 115)
"#;

    let _with_newline = r#"
this is a very long string exceeded maximum width in this case maximum 100. (current this line width is about 115)
"#;
}


