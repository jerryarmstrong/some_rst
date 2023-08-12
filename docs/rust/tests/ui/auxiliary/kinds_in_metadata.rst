tests/ui/auxiliary/kinds_in_metadata.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /* Any copyright is dedicated to the Public Domain.
 * http://creativecommons.org/publicdomain/zero/1.0/ */

// Tests that metadata serialization works for the `Copy` kind.

#![crate_type="lib"]

pub fn f<T:Copy>() {}


