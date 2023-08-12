src/tools/rustfmt/tests/target/issue-2479.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Long attributes.
#[derive(Clone, Copy, Debug, PartialEq)]
pub enum POLARITYR {
    #[doc = "Task mode: No effect on pin from OUT[n] task. Event mode: no IN[n] event generated on pin activity."]
    NONE,
    #[doc = "Task mode: Set pin from OUT[n] task. Event mode: Generate IN[n] event when rising edge on pin."]
    LOTOHI,
    #[doc = "Task mode: Clear pin from OUT[n] task. Event mode: Generate IN[n] event when falling edge on pin."]
    HITOLO,
    #[doc = "Task mode: Toggle pin from OUT[n]. Event mode: Generate IN[n] when any change on pin."]
    TOGGLE,
}


