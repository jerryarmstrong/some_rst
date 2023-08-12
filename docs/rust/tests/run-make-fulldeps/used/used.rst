tests/run-make-fulldeps/used/used.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[used]
static FOO: u32 = 0;

static BAR: u32 = 0;


