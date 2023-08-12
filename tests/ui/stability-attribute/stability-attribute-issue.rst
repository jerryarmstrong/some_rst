tests/ui/stability-attribute/stability-attribute-issue.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:stability_attribute_issue.rs
#![deny(deprecated)]

extern crate stability_attribute_issue;
use stability_attribute_issue::*;

fn main() {
    unstable();
    //~^ ERROR use of unstable library feature 'unstable_test_feature'
    unstable_msg();
    //~^ ERROR use of unstable library feature 'unstable_test_feature': message
}


