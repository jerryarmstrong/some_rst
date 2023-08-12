tests/ui/cfg/cfg-method-receiver-ok.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! foo {
    () => {
        #[allow(unreachable_patterns)]
        {
            123i32
        }
    };
}

fn main() {
    let _ = foo!().abs();
}


