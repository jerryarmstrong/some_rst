src/tools/rustfmt/tests/source/issue-3270/one.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: One

pub fn main() {
    /*   let s = String::from(
        "
hello
world
",
    ); */

    assert_eq!(s, "\nhello\nworld\n");
}


