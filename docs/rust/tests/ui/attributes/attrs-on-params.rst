tests/ui/attributes/attrs-on-params.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This checks that incorrect params on function parameters are caught

fn function(#[inline] param: u32) {
    //~^ ERROR attribute should be applied to function or closure
    //~| ERROR allow, cfg, cfg_attr, deny, expect, forbid, and warn are the only allowed built-in attributes
}

fn main() {}


