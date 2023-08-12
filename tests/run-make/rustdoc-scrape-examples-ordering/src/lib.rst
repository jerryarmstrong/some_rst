tests/run-make/rustdoc-scrape-examples-ordering/src/lib.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has foobar/fn.ok.html '//*[@class="docblock scraped-example-list"]' 'ex2'
// @has foobar/fn.ok.html '//*[@class="more-scraped-examples"]' 'ex1'
// @has foobar/fn.ok.html '//*[@class="highlight focus"]' 'ok'
// @has foobar/fn.ok.html '//*[@class="highlight"]' 'ok'

pub fn ok(_x: i32) {}


