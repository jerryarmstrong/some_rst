src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0032_fn_pointer_type.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = fn();
type B = unsafe fn();
type C = unsafe extern "C" fn();
type D = extern "C" fn ( u8 , ... ) -> u8;


