tests/codegen-units/partitioning/auxiliary/cgu_extern_drop_glue.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

pub struct Struct(pub u32);

impl Drop for Struct {
    fn drop(&mut self) {}
}


