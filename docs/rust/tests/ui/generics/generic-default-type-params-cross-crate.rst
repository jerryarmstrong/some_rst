tests/ui/generics/generic-default-type-params-cross-crate.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:default_type_params_xc.rs

// pretty-expanded FIXME #23616

extern crate default_type_params_xc;

struct Vec<T, A = default_type_params_xc::Heap>(#[allow(unused_tuple_struct_fields)] Option<(T,A)>);

struct Foo;

fn main() {
    let _a = Vec::<isize>(None);
    let _b = Vec::<isize, default_type_params_xc::FakeHeap>(None);
    let _c = default_type_params_xc::FakeVec::<isize> { f: None };
    let _d = default_type_params_xc::FakeVec::<isize, Foo> { f: None };
}


