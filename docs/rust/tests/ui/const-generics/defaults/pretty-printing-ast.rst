tests/ui/const-generics/defaults/pretty-printing-ast.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the AST pretty printer correctly handles default values for const generics
// check-pass
// compile-flags: -Z unpretty=expanded

#![crate_type = "lib"]

trait Foo<const KIND: bool = true> {}

fn foo<const SIZE: usize = 5>() {}

struct Range<const FROM: usize = 0, const LEN: usize = 0, const TO: usize = FROM>;


