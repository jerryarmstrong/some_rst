tests/ui/ret-non-nil.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: `return;` in a function whose return type is not `()`

fn f() { return; }

fn g() -> isize { return; }

fn main() { f(); g(); }


