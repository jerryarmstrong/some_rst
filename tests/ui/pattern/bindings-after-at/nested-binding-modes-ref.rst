tests/ui/pattern/bindings-after-at/nested-binding-modes-ref.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let ref is_ref @ is_val = 42;
    *is_ref;
    *is_val;
    //~^ ERROR cannot be dereferenced

    let is_val @ ref is_ref = 42;
    *is_ref;
    *is_val;
    //~^ ERROR cannot be dereferenced
}


