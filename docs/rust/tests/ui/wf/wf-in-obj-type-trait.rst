tests/ui/wf/wf-in-obj-type-trait.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we enforce WF conditions also for types in fns.

trait Object<T> { }

struct MustBeCopy<T:Copy> {
    t: T
}

struct Bar<T> {
    // needs T: Copy
    x: dyn Object<MustBeCopy<T>> //~ ERROR E0277
}

fn main() { }


