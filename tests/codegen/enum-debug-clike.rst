tests/codegen/enum-debug-clike.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This tests that debug info for "c-like" enums is properly emitted.
// This is ignored for the fallback mode on MSVC due to problems with PDB.

//
// ignore-msvc

// compile-flags: -g -C no-prepopulate-passes

// CHECK-LABEL: @main
// CHECK: {{.*}}DICompositeType{{.*}}tag: DW_TAG_enumeration_type,{{.*}}name: "E",{{.*}}flags: DIFlagEnumClass,{{.*}}
// CHECK: {{.*}}DIEnumerator{{.*}}name: "A",{{.*}}value: {{[0-9].*}}
// CHECK: {{.*}}DIEnumerator{{.*}}name: "B",{{.*}}value: {{[0-9].*}}
// CHECK: {{.*}}DIEnumerator{{.*}}name: "C",{{.*}}value: {{[0-9].*}}

#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]

enum E { A, B, C }

pub fn main() {
    let e = E::C;
}


