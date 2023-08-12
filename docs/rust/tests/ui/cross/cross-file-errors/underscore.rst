tests/ui/cross/cross-file-errors/underscore.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We want this file only so we can test cross-file error
// messages, but we don't want it in an external crate.
// ignore-test
#![crate_type = "lib"]

macro_rules! underscore {
    () => (
        _
    )
}


