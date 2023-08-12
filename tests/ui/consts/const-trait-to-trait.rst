tests/ui/consts/const-trait-to-trait.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
// Issue #24644 - block causes a &Trait -> &Trait coercion:
trait Trait {}

struct Bar;
impl Trait for Bar {}

fn main() {
    let x: &[&dyn Trait] = &[{ &Bar }];
}

// Issue #25748 - the cast causes an &Encoding -> &Encoding coercion:
pub struct UTF8Encoding;
pub const UTF_8: &'static UTF8Encoding = &UTF8Encoding;
pub trait Encoding {}
impl Encoding for UTF8Encoding {}
pub fn f() -> &'static dyn Encoding { UTF_8 as &'static dyn Encoding }

// Root of the problem: &Trait -> &Trait coercions:
const FOO: &'static dyn Trait = &Bar;
const BAR: &'static dyn Trait = FOO;
fn foo() { let _x = BAR; }


