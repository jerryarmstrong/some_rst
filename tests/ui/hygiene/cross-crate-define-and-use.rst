tests/ui/hygiene/cross-crate-define-and-use.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that a marco from another crate can define an item in one expansion
// and use it from another, without it being visible to everyone.
// This requires that the definition of `my_struct` preserves the hygiene
// information for the tokens in its definition.

// check-pass
// aux-build:use_by_macro.rs

#![feature(type_name_of_val)]
extern crate use_by_macro;

use use_by_macro::*;

enum MyStruct {}
my_struct!(define);

fn main() {
    let x = my_struct!(create);
}


