tests/ui/coherence/coherence-impls-sized.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

use std::marker::Copy;

enum TestE {
  A
}

struct MyType;

struct NotSync;
impl !Sync for NotSync {}

impl Sized for TestE {}
//~^ ERROR E0322

impl Sized for MyType {}
//~^ ERROR E0322

impl Sized for (MyType, MyType) {}
//~^ ERROR E0322
//~| ERROR E0117

impl Sized for &'static NotSync {}
//~^ ERROR E0322

impl Sized for [MyType] {}
//~^ ERROR E0322
//~| ERROR E0117

impl Sized for &'static [NotSync] {}
//~^ ERROR E0322
//~| ERROR E0117

fn main() {
}


