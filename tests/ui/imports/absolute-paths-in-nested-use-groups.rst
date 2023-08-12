tests/ui/imports/absolute-paths-in-nested-use-groups.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_imports)]

mod foo {}

use foo::{
    ::bar,       //~ ERROR crate root in paths can only be used in start position
    super::bar,  //~ ERROR `super` in paths can only be used in start position
    self::bar,   //~ ERROR `self` in paths can only be used in start position
};

fn main() {}


