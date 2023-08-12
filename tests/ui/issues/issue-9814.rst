tests/ui/issues/issue-9814.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verify that single-variant enums can't be de-referenced
// Regression test for issue #9814

enum Foo { Bar(isize) }

fn main() {
    let _ = *Foo::Bar(2); //~ ERROR type `Foo` cannot be dereferenced
}


