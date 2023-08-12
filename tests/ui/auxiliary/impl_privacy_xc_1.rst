tests/ui/auxiliary/impl_privacy_xc_1.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

pub struct Fish {
    pub x: isize
}

impl Fish {
    pub fn swim(&self) {}
}


