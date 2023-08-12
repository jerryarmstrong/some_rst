tests/ui/wf/wf-in-fn-where-clause.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we enforce WF conditions also for where clauses in fn items.


#![allow(dead_code)]

trait MustBeCopy<T:Copy> {
}

fn bar<T,U>()
    where T: MustBeCopy<U> //~ ERROR E0277
{
}


fn main() { }


