tests/ui/associated-types/associated-type-macro.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    #[cfg(FALSE)]
    <() as module>::mac!(); //~ ERROR macros cannot use qualified paths
}


