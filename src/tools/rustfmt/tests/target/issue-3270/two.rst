src/tools/rustfmt/tests/target/issue-3270/two.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

pub fn main() {
    /*   let s = String::from(
        "
hello
world
",
    ); */

    assert_eq!(s, "\nhello\nworld\n");
}


