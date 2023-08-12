tests/rustdoc-ui/doc-cfg.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(doc_cfg)]

#[doc(cfg(), cfg(foo, bar))]
//~^ ERROR
//~^^ ERROR
#[doc(cfg(foo), cfg(bar))] // ok!
#[doc(cfg())] //~ ERROR
#[doc(cfg(foo, bar))] //~ ERROR
pub fn foo() {}


