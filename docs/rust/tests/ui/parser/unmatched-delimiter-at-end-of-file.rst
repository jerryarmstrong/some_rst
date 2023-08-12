tests/ui/parser/unmatched-delimiter-at-end-of-file.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    x: usize,
    y: usize,
}

fn main() {
    S { x: 4,
        y: 5 };
}

fn foo() { //~ ERROR this file contains an unclosed delimiter


