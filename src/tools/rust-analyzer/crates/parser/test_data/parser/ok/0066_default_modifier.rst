src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0066_default_modifier.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
  default type T = Bar;
  default const f: u8 = 0;
  default fn foo() {}
  default unsafe fn bar() {}
}

impl T for Foo {
  default type T = Bar;
  default const f: u8 = 0;
  default fn foo() {}
  default unsafe fn bar() {}
}

default impl T for () {}
default unsafe impl T for () {}


