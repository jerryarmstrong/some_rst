src/tools/clippy/tests/ui/rc_mutex.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::rc_mutex)]
#![allow(unused, clippy::disallowed_names)]

use std::rc::Rc;
use std::sync::Mutex;

pub struct MyStructWithPrivItem {
    foo: Rc<Mutex<i32>>,
}

pub struct MyStructWithPubItem {
    pub foo: Rc<Mutex<i32>>,
}

pub struct SubT<T> {
    foo: T,
}

pub enum MyEnum {
    One,
    Two,
}

// All of these test should be trigger the lint because they are not
// part of the public api
fn test1<T>(foo: Rc<Mutex<T>>) {}
fn test2(foo: Rc<Mutex<MyEnum>>) {}
fn test3(foo: Rc<Mutex<SubT<usize>>>) {}

// All of these test should be allowed because they are part of the
// public api and `avoid_breaking_exported_api` is `false` by default.
pub fn pub_test1<T>(foo: Rc<Mutex<T>>) {}
pub fn pub_test2(foo: Rc<Mutex<MyEnum>>) {}
pub fn pub_test3(foo: Rc<Mutex<SubT<usize>>>) {}

fn main() {}


