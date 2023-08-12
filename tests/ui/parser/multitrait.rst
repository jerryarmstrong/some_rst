tests/ui/parser/multitrait.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
 y: isize
}

impl Cmp, ToString for S {
//~^ ERROR: expected one of `!`, `(`, `+`, `::`, `<`, `for`, `where`, or `{`, found `,`
  fn eq(&&other: S) { false }
  fn to_string(&self) -> String { "hi".to_string() }
}


