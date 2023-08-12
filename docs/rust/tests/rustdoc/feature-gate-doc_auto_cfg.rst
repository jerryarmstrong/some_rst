tests/rustdoc/feature-gate-doc_auto_cfg.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(doc_cfg)]

#![crate_name = "foo"]

// @has foo/fn.foo.html
// @count - '//*[@class="item-info"]/*[@class="stab portability"]' 0
#[cfg(not(test))]
pub fn foo() {}


