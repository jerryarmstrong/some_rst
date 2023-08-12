tests/ui/lint/crate_level_only_lint.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(uncommon_codepoints, unused_attributes)]

mod foo {
#![allow(uncommon_codepoints)]
//~^ ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
//~| ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
//~| ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]

#[allow(uncommon_codepoints)]
//~^ ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
//~| ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
//~| ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
const BAR: f64 = 0.000001;

}

#[allow(uncommon_codepoints)]
//~^ ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
//~| ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
//~| ERROR allow(uncommon_codepoints) is ignored unless specified at crate level [unused_attributes]
fn main() {
}


