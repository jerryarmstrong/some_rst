tests/ui/layout/debug.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test "pref: Align\([1-8] bytes\)" -> "pref: $$PREF_ALIGN"
#![feature(never_type, rustc_attrs, type_alias_impl_trait)]
#![crate_type = "lib"]

#[rustc_layout(debug)]
enum E { Foo, Bar(!, i32, i32) } //~ ERROR: layout_of

#[rustc_layout(debug)]
struct S { f1: i32, f2: (), f3: i32 } //~ ERROR: layout_of

#[rustc_layout(debug)]
union U { f1: (i32, i32), f3: i32 } //~ ERROR: layout_of

#[rustc_layout(debug)]
type Test = Result<i32, i32>; //~ ERROR: layout_of

#[rustc_layout(debug)]
type T = impl std::fmt::Debug; //~ ERROR: layout_of

fn f() -> T {
    0i32
}


