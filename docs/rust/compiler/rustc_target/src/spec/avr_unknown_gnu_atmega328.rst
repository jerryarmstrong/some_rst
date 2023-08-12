compiler/rustc_target/src/spec/avr_unknown_gnu_atmega328.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;

pub fn target() -> Target {
    super::avr_gnu_base::target("atmega328", "-mmcu=atmega328")
}


