tests/ui/lifetimes/issue-83907-invalid-fn-like-path.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

static STATIC_VAR_FIVE: &One();
//~^ cannot find type
//~| free static item without body

fn main() {}


