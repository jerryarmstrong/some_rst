src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0081_for_type.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = for<'a> fn() -> ();
type B = for<'a> unsafe extern "C" fn(&'a ()) -> ();
type Obj = for<'a> PartialEq<&'a i32>;


