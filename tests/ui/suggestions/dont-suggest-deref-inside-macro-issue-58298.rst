tests/ui/suggestions/dont-suggest-deref-inside-macro-issue-58298.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn warn(_: &str) {}

macro_rules! intrinsic_match {
    ($intrinsic:expr) => {
        warn(format!("unsupported intrinsic {}", $intrinsic));
        //~^ ERROR mismatched types
    };
}

fn main() {
    intrinsic_match! {
        "abc"
    };
}


