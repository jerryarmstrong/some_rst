tests/ui/wf/wf-in-fn-arg.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we enforce WF conditions also for argument types in fn items.

#![feature(rustc_attrs)]
#![allow(dead_code)]

struct MustBeCopy<T:Copy> {
    t: T
}

fn bar<T>(_: &MustBeCopy<T>) //~ ERROR E0277
{
}

fn main() { }


