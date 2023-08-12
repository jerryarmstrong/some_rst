tests/ui/feature-gates/feature-gate-concat_idents2.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    concat_idents!(a, b); //~ ERROR `concat_idents` is not stable enough
                          //~| ERROR cannot find value `ab` in this scope
}


