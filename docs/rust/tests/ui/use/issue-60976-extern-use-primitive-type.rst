tests/ui/use/issue-60976-extern-use-primitive-type.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #60976: ICE (with <=1.36.0) when another file had `use <primitive_type>;`.
// check-pass
// aux-build:extern-use-primitive-type-lib.rs

extern crate extern_use_primitive_type_lib;

fn main() {}


