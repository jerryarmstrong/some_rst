tests/run-make/rustdoc-scrape-examples-whitespace/examples/ex.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;
impl Foo {
  fn bar() { foobar::ok(); }
}

fn main() {
  Foo::bar();
}


