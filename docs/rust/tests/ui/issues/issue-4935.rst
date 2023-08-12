tests/ui/issues/issue-4935.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #4935

fn foo(a: usize) {}
//~^ defined here
fn main() { foo(5, 6) }
//~^ ERROR function takes 1 argument but 2 arguments were supplied


