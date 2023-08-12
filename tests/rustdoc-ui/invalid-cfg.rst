tests/rustdoc-ui/invalid-cfg.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(doc_cfg)]
#[doc(cfg = "x")] //~ ERROR not followed by parentheses
#[doc(cfg(x, y))] //~ ERROR multiple `cfg` predicates
struct S {}


