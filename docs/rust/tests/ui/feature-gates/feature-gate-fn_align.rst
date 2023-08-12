tests/ui/feature-gates/feature-gate-fn_align.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[repr(align(16))] //~ ERROR `repr(align)` attributes on functions are unstable
fn requires_alignment() {}


