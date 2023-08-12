tests/ui/feature-gates/feature-gate-unsized_locals.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(f: dyn FnOnce()) {}
//~^ ERROR E0277

fn main() {
}


