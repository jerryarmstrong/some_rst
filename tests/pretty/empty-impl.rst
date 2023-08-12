tests/pretty/empty-impl.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

trait X { fn dummy(&self) { } }
impl X for usize { }

trait Y { fn dummy(&self) { } }
impl Y for usize { }


