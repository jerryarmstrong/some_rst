tests/ui/feature-gates/feature-gate-unsized_tuple_coercion.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ : &(dyn Send,) = &((),);
    //~^ ERROR unsized tuple coercion is not stable enough
}


