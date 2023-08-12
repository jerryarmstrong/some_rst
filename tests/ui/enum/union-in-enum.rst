tests/ui/enum/union-in-enum.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that the union keyword
// is accepted as the name of an enum variant
// when not followed by an identifier
// This special case exists because `union` is a contextual keyword.

#![allow(warnings)]

// check-pass

enum A { union }
enum B { union {} }
enum C { union() }
fn main(){}


