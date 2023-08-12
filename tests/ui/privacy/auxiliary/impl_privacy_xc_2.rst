tests/ui/privacy/auxiliary/impl_privacy_xc_2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

pub struct Fish {
    pub x: isize
}

mod unexported {
    use super::Fish;
    impl PartialEq for Fish {
        fn eq(&self, _: &Fish) -> bool { true }
        fn ne(&self, _: &Fish) -> bool { false }
    }
}


