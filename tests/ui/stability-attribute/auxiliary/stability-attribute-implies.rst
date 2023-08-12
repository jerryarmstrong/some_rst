tests/ui/stability-attribute/auxiliary/stability-attribute-implies.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "stability_attribute_implies", since = "1.0.0")]

#[stable(feature = "foo", since = "1.62.0")]
pub fn foo() {}

#[unstable(feature = "foobar", issue = "1", implied_by = "foo")]
pub fn foobar() {}


