tests/run-make/rustdoc-scrape-examples-remap/src/lib.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has foobar/b/fn.foo.html '//*[@class="scraped-example expanded"]' 'ex.rs'
// @has foobar/c/fn.foo.html '//*[@class="scraped-example expanded"]' 'ex.rs'

#[path = "a.rs"]
pub mod b;

#[path = "a.rs"]
pub mod c;


