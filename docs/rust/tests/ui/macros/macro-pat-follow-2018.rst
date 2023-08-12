tests/ui/macros/macro-pat-follow-2018.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// edition:2018

macro_rules! pat_bar {
    ($p:pat | $p2:pat) => {{
        match Some(1u8) {
            $p | $p2 => {}
            _ => {}
        }
    }};
}

fn main() {
    pat_bar!(Some(1u8) | None);
}


