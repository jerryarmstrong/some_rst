tests/rustdoc-ui/intra-doc/auxiliary/pointer-reexports-allowed.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intra_doc_pointers)]
#![crate_name = "inner"]
/// Link to [some pointer](*const::to_raw_parts)
pub fn foo() {}


