tests/ui/hygiene/auxiliary/nested-dollar-crate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub const IN_DEF_CRATE: &str = "In def crate!";

macro_rules! make_it {
    () => {
        #[macro_export]
        macro_rules! inner {
            () => {
                $crate::IN_DEF_CRATE
            }
        }
    }
}

make_it!();


