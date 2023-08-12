tests/ui/missing_debug_impls.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type lib
#![deny(missing_debug_implementations)]
#![allow(unused)]

use std::fmt;

pub enum A {} //~ ERROR type does not implement `Debug`

#[derive(Debug)]
pub enum B {}

pub enum C {}

impl fmt::Debug for C {
    fn fmt(&self, fmt: &mut fmt::Formatter) -> fmt::Result {
        Ok(())
    }
}

pub struct Foo; //~ ERROR type does not implement `Debug`

#[derive(Debug)]
pub struct Bar;

pub struct Baz;

impl fmt::Debug for Baz {
    fn fmt(&self, fmt: &mut fmt::Formatter) -> fmt::Result {
        Ok(())
    }
}

struct PrivateStruct;

enum PrivateEnum {}

#[derive(Debug)]
struct GenericType<T>(T);


