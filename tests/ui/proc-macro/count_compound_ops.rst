tests/ui/proc-macro/count_compound_ops.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:count_compound_ops.rs

extern crate count_compound_ops;
use count_compound_ops::count_compound_ops;

fn main() {
    assert_eq!(count_compound_ops!(foo<=>bar <<<! -baz ++), 4);
}


