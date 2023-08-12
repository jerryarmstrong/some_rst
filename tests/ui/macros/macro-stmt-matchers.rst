tests/ui/macros/macro-stmt-matchers.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)


fn main() {
    macro_rules! m { ($s:stmt;) => { $s } }
    m!(vec![].push(0););
}


