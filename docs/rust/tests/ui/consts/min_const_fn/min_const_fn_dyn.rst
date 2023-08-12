tests/ui/consts/min_const_fn/min_const_fn_dyn.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct HasDyn {
    field: &'static dyn std::fmt::Debug,
}

struct Hide(HasDyn);

const fn no_inner_dyn_trait(_x: Hide) {}
const fn no_inner_dyn_trait2(x: Hide) {
    x.0.field;
}
const fn no_inner_dyn_trait_ret() -> Hide { Hide(HasDyn { field: &0 }) }

fn main() {}


