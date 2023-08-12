tests/rustdoc/synthetic_auto/crate-local.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]

pub auto trait Banana {}

// @has crate_local/struct.Peach.html
// @has - '//h3[@class="code-header"]' 'impl Banana for Peach'
// @has - '//h3[@class="code-header"]' 'impl Send for Peach'
// @has - '//h3[@class="code-header"]' 'impl Sync for Peach'
pub struct Peach;


