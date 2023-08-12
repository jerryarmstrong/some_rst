tests/ui/macros/auxiliary/macro_with_super_1.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[macro_export]
macro_rules! declare {
    () => (
        pub fn aaa() {}

        pub mod bbb {
            use super::aaa;

            pub fn ccc() {
                aaa();
            }
        }
    )
}


