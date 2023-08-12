tests/ui/imports/unresolved-imports-used.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // There should be *one* unused import error.
#![deny(unused_imports)]

mod qux {
   fn quz() {}
   pub fn quy() {}
}

use qux::quz;  //~ ERROR function `quz` is private
use qux::bar;  //~ ERROR unresolved import `qux::bar`
use foo::bar;  //~ ERROR unresolved import `foo`
use baz::*;    //~ ERROR unresolved import `baz`
use qux::bar2; //~ ERROR unresolved import `qux::bar2`
use foo2::bar2;//~ ERROR unresolved import `foo2`
use baz2::*;   //~ ERROR unresolved import `baz2`
use qux::quy;  //~ ERROR unused import

fn main() {}


