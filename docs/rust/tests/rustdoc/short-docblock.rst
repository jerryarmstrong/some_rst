tests/rustdoc/short-docblock.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/index.html '//*[@class="item-right docblock-short"]' 'fooo'
// @!has foo/index.html '//*[@class="item-right docblock-short"]/h1' 'fooo'
// @has foo/fn.foo.html '//h2[@id="fooo"]/a[@href="#fooo"]' 'fooo'

/// # fooo
///
/// foo
pub fn foo() {}

// @has foo/index.html '//*[@class="item-right docblock-short"]' 'mooood'
// @!has foo/index.html '//*[@class="item-right docblock-short"]/h2' 'mooood'
// @has foo/foo/index.html '//h3[@id="mooood"]/a[@href="#mooood"]' 'mooood'

/// ## mooood
///
/// foo mod
pub mod foo {}

// @has foo/index.html '//*[@class="item-right docblock-short"]/a[@href=\
//                      "https://nougat.world"]/code' 'nougat'

/// [`nougat`](https://nougat.world)
pub struct Bar;


