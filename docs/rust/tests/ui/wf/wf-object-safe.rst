tests/ui/wf/wf-object-safe.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that object-safe traits are not WF when used as object types.
// Issue #21953.

trait A {
    fn foo(&self, _x: &Self);
}

fn main() {
    let _x: &dyn A; //~ ERROR E0038
}


