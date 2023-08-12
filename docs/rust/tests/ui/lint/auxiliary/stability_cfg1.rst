tests/ui/lint/auxiliary/stability_cfg1.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![cfg_attr(foo, experimental)]
#![cfg_attr(not(foo), stable(feature = "test_feature", since = "1.0.0"))]
#![feature(staged_api)]


