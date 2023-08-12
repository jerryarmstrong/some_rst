tests/ui/proc-macro/attr-complex-fn.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z span-debug --error-format human
// aux-build:test-macros.rs

#![feature(stmt_expr_attributes)]
#![feature(custom_inner_attributes)]
#![feature(rustc_attrs)]

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;

trait MyTrait<T> {}
struct MyStruct<const N: bool>;

#[print_attr]
fn foo<T: MyTrait<MyStruct<{ true }>>>() {}

impl<T> MyTrait<T> for MyStruct<{true}> {
    #![print_attr]
    #![rustc_dummy]
}

fn main() {}


