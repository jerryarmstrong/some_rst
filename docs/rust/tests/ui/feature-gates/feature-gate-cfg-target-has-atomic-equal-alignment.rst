tests/ui/feature-gates/feature-gate-cfg-target-has-atomic-equal-alignment.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    cfg!(target_has_atomic_equal_alignment = "8");
    //~^ ERROR `cfg(target_has_atomic_equal_alignment)` is experimental and subject to change
    cfg!(target_has_atomic_equal_alignment = "16");
    //~^ ERROR `cfg(target_has_atomic_equal_alignment)` is experimental and subject to change
    cfg!(target_has_atomic_equal_alignment = "32");
    //~^ ERROR `cfg(target_has_atomic_equal_alignment)` is experimental and subject to change
    cfg!(target_has_atomic_equal_alignment = "64");
    //~^ ERROR `cfg(target_has_atomic_equal_alignment)` is experimental and subject to change
    cfg!(target_has_atomic_equal_alignment = "128");
    //~^ ERROR `cfg(target_has_atomic_equal_alignment)` is experimental and subject to change
    cfg!(target_has_atomic_equal_alignment = "ptr");
    //~^ ERROR `cfg(target_has_atomic_equal_alignment)` is experimental and subject to change
}


