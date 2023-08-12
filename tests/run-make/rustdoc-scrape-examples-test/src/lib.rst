tests/run-make/rustdoc-scrape-examples-test/src/lib.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has foobar/fn.ok.html '//*[@class="docblock scraped-example-list"]' ''

pub fn ok() {}


