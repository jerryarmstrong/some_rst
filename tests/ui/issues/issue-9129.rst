tests/ui/issues/issue-9129.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
// ignore-pretty unreported

pub trait bomb { fn boom(&self, _: Ident); }
pub struct S;
impl bomb for S { fn boom(&self, _: Ident) { } }

pub struct Ident { name: usize }

macro_rules! int3 { () => ( { } ) }

fn Ident_new() -> Ident {
    int3!();
    Ident {name: 0x6789ABCD }
}

pub fn light_fuse(fld: Box<dyn bomb>) {
    int3!();
    let f = || {
        int3!();
        fld.boom(Ident_new()); // *** 1
    };
    f();
}

pub fn main() {
    let b = Box::new(S) as Box<dyn bomb>;
    light_fuse(b);
}


