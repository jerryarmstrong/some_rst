tests/rustdoc-ui/intra-doc/double-anchor.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// regression test for #73264
// should only give one error
/// docs [label][with#anchor#error]
//~^ WARNING multiple anchors
pub struct S;


