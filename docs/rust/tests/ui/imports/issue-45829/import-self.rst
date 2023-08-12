tests/ui/imports/issue-45829/import-self.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub struct A;
    pub struct B;
}

use foo::{self};
//~^ ERROR is defined multiple times

use foo as self;
//~^ ERROR expected identifier

use foo::self; //~ ERROR is defined multiple times
//~^ ERROR `self` imports are only allowed within a { } list

use foo::A;
use foo::{self as A};
//~^ ERROR is defined multiple times

fn main() {}


