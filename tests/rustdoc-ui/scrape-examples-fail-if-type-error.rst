tests/rustdoc-ui/scrape-examples-fail-if-type-error.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
// compile-flags: -Z unstable-options --scrape-examples-output-path {{build-base}}/t.calls --scrape-examples-target-crate foobar

pub fn foo() {
  INVALID_FUNC();
  //~^ ERROR could not resolve path
}


