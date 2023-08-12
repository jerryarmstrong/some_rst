tests/incremental/link_order/auxiliary/my_lib.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
//[cfail1] compile-flags: -lbar -lfoo --crate-type lib -Zassert-incr-state=not-loaded
//[cfail2] compile-flags: -lfoo -lbar --crate-type lib -Zassert-incr-state=not-loaded


