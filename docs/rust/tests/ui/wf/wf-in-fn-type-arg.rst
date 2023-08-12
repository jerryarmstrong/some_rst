tests/ui/wf/wf-in-fn-type-arg.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we enforce WF conditions also for types in fns.

struct MustBeCopy<T:Copy> {
    t: T
}

struct Bar<T> {
    // needs T: Copy
    x: fn(MustBeCopy<T>) //~ ERROR E0277
}

fn main() { }


