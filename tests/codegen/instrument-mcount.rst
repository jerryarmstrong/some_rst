tests/codegen/instrument-mcount.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// compile-flags: -Z instrument-mcount

#![crate_type = "lib"]

// CHECK: attributes #{{.*}} "frame-pointer"="all" "instrument-function-entry-inlined"="{{.*}}mcount{{.*}}"
pub fn foo() {}


