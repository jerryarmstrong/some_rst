tests/ui/coherence/auxiliary/coherence_inherent_cc_lib.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See coherence_inherent_cc.rs

pub trait TheTrait {
    fn the_fn(&self);
}

pub struct TheStruct;

impl TheTrait for TheStruct {
    fn the_fn(&self) {}
}


