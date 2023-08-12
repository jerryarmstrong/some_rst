tests/codegen/noreturnflag.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -g -C no-prepopulate-passes

#![crate_type = "lib"]

#[no_mangle]
pub fn foo() -> ! {
// CHECK: @foo() unnamed_addr #0
    loop {}
}

pub enum EmptyEnum {}

#[no_mangle]
pub fn bar() -> EmptyEnum {
// CHECK: @bar() unnamed_addr #0
    loop {}
}

// CHECK: attributes #0 = {{{.*}} noreturn {{.*}}}

// CHECK: DISubprogram(name: "foo", {{.*}} DIFlagNoReturn
// CHECK: DISubprogram(name: "bar", {{.*}} DIFlagNoReturn


