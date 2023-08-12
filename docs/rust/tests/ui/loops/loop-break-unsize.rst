tests/ui/loops/loop-break-unsize.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #62312
// check-pass

fn main() {
    let _ = loop {
        break Box::new(()) as Box<dyn Send>;
    };
}


