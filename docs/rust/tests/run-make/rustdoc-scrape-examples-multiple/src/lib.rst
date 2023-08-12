tests/run-make/rustdoc-scrape-examples-multiple/src/lib.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has foobar/fn.ok.html '//*[@class="docblock scraped-example-list"]//*[@class="prev"]' ''
// @has foobar/fn.ok.html '//*[@class="more-scraped-examples"]' ''
// @has src/ex/ex.rs.html
// @has foobar/fn.ok.html '//a[@href="../src/ex/ex.rs.html#2"]' ''

pub fn ok() {}


