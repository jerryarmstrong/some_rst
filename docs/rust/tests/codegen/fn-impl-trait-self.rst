tests/codegen/fn-impl-trait-self.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -g
//
// CHECK-LABEL: @main
// MSVC: {{.*}}DIDerivedType(tag: DW_TAG_pointer_type, name: "recursive_type$ (*)()",{{.*}}
// NONMSVC: {{.*}}DIDerivedType(tag: DW_TAG_pointer_type, name: "fn() -> <recursive_type>",{{.*}}
//
// CHECK: {{.*}}DISubroutineType{{.*}}
// CHECK: {{.*}}DIBasicType(name: "<recur_type>", size: {{32|64}}, encoding: DW_ATE_unsigned)

pub fn foo() -> impl Copy {
    foo
}

fn main() {
    let my_res = foo();
}


