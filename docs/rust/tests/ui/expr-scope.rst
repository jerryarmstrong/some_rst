tests/ui/expr-scope.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Regression test for issue #762

// pretty-expanded FIXME #23616

pub fn f() { }
pub fn main() { return ::f(); }


