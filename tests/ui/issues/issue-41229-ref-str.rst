tests/ui/issues/issue-41229-ref-str.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn example(ref s: str) {}
//~^ ERROR the size for values of type

fn main() {}


