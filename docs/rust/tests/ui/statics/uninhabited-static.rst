tests/ui/statics/uninhabited-static.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![deny(uninhabited_static)]

enum Void {}
extern {
    static VOID: Void; //~ ERROR static of uninhabited type
    //~| WARN: previously accepted
    static NEVER: !; //~ ERROR static of uninhabited type
    //~| WARN: previously accepted
}

static VOID2: Void = unsafe { std::mem::transmute(()) }; //~ ERROR static of uninhabited type
//~| WARN: previously accepted
//~| ERROR could not evaluate static initializer
//~| WARN: type `Void` does not permit zero-initialization
static NEVER2: Void = unsafe { std::mem::transmute(()) }; //~ ERROR static of uninhabited type
//~| WARN: previously accepted
//~| ERROR could not evaluate static initializer
//~| WARN: type `Void` does not permit zero-initialization

fn main() {}


