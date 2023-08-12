src/tools/rustfmt/tests/target/issue-4245.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(
    a: & // Comment
    // Another comment
    'a File,
) {
}

fn b(b: & /* Another Comment */ 'a File) {}

fn c(c: &'a /*Comment */ mut /*Comment */ File) {}

fn d(
    c: & // Comment
    'b // Multi Line
    // Comment
    mut // Multi Line
    // Comment
    File,
) {
}

fn e(
    c: & // Comment
    File,
) {
}

fn d(
    c: & // Comment
    mut // Multi Line
    // Comment
    File,
) {
}


