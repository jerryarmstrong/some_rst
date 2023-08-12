tests/ui/definition-reachable/field-method.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that functions accessible through a field visible to a macro are
// considered reachable

// aux-build:nested-fn-macro.rs
// run-pass

extern crate nested_fn_macro;

fn main() {
    assert_eq!(nested_fn_macro::m!(), 12);
}


