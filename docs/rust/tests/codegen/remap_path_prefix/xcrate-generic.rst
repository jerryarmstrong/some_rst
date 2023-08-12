tests/codegen/remap_path_prefix/xcrate-generic.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-windows
// compile-flags: -g -C metadata=foo -C no-prepopulate-passes
// aux-build:xcrate-generic.rs

#![crate_type = "lib"]

extern crate xcrate_generic;

pub fn foo() {
    xcrate_generic::foo::<u32>();
}

// Here we check that local debuginfo is mapped correctly.
// CHECK: !DIFile(filename: "/the/aux-src/xcrate-generic.rs", directory: ""


