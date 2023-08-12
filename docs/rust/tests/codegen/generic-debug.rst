tests/codegen/generic-debug.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-windows

// compile-flags: -g -C no-prepopulate-passes

// CHECK-LABEL: @main
// CHECK: {{.*}}DICompositeType{{.*}}tag: DW_TAG_structure_type,{{.*}}name: "Generic<i32>",{{.*}}
// CHECK: {{.*}}DITemplateTypeParameter{{.*}}name: "Type",{{.*}}

#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]

pub struct Generic<Type>(Type);

fn main () {
    let generic = Generic(10);
}


