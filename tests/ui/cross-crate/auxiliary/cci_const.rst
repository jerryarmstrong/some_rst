tests/ui/cross-crate/auxiliary/cci_const.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub extern "C" fn bar() {
}

pub const foopy: &'static str = "hi there";
pub const uint_val: usize = 12;
pub const uint_expr: usize = (1 << uint_val) - 1;


