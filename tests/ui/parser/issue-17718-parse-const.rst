tests/ui/parser/issue-17718-parse-const.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

const FOO: usize = 3;

fn main() {
    assert_eq!(FOO, 3);
}


