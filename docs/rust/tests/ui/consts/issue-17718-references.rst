tests/ui/consts/issue-17718-references.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

struct Struct { a: usize }

const C: usize = 1;
static S: usize = 1;

const T1: &'static usize = &C;
const T2: &'static usize = &S; //~ ERROR: constants cannot refer to statics
static T3: &'static usize = &C;
static T4: &'static usize = &S;

const T5: usize = C;
const T6: usize = S; //~ ERROR: constants cannot refer to statics
static T7: usize = C;
static T8: usize = S;

const T9: Struct = Struct { a: C };
const T10: Struct = Struct { a: S };
//~^ ERROR: constants cannot refer to statics
static T11: Struct = Struct { a: C };
static T12: Struct = Struct { a: S };

fn main() {}


