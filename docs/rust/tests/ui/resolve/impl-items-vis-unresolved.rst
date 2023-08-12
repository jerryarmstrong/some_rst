tests/ui/resolve/impl-items-vis-unresolved.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Visibilities on impl items expanded from macros are resolved (issue #64705).

macro_rules! perftools_inline {
    ($($item:tt)*) => (
        $($item)*
    );
}

mod state {
    pub struct RawFloatState;
    impl RawFloatState {
        perftools_inline! {
            pub(super) fn new() {} // OK
        }
    }
}

pub struct RawFloatState;
impl RawFloatState {
    perftools_inline! {
        pub(super) fn new() {}
        //~^ ERROR failed to resolve: there are too many leading `super` keywords
    }
}

fn main() {}


