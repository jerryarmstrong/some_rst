tests/ui/rfcs/rfc-2396-target_feature-11/fn-traits.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64

#![feature(target_feature_11)]

#[target_feature(enable = "avx")]
fn foo() {}

#[target_feature(enable = "avx")]
unsafe fn foo_unsafe() {}

fn call(f: impl Fn()) {
    f()
}

fn call_mut(f: impl FnMut()) {
    f()
}

fn call_once(f: impl FnOnce()) {
    f()
}

fn main() {
    call(foo); //~ ERROR expected a `Fn<()>` closure, found `fn() {foo}`
    call_mut(foo); //~ ERROR expected a `FnMut<()>` closure, found `fn() {foo}`
    call_once(foo); //~ ERROR expected a `FnOnce<()>` closure, found `fn() {foo}`

    call(foo_unsafe);
    //~^ ERROR expected a `Fn<()>` closure, found `unsafe fn() {foo_unsafe}`
    call_mut(foo_unsafe);
    //~^ ERROR expected a `FnMut<()>` closure, found `unsafe fn() {foo_unsafe}`
    call_once(foo_unsafe);
    //~^ ERROR expected a `FnOnce<()>` closure, found `unsafe fn() {foo_unsafe}`
}


