tests/ui/lifetimes/issue-90170-elision-mismatch.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub fn foo(x: &mut Vec<&u8>, y: &u8) { x.push(y); } //~ ERROR lifetime may not live long enough

pub fn foo2(x: &mut Vec<&'_ u8>, y: &u8) { x.push(y); } //~ ERROR lifetime may not live long enough

pub fn foo3<'a>(_other: &'a [u8], x: &mut Vec<&u8>, y: &u8) { x.push(y); } //~ ERROR lifetime may not live long enough

fn main() {}


