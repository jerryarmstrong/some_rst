tests/ui/issues/issue-7364.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::RefCell;

// Regression test for issue 7364
static boxed: Box<RefCell<isize>> = Box::new(RefCell::new(0));
//~^ ERROR `RefCell<isize>` cannot be shared between threads safely [E0277]

fn main() { }


