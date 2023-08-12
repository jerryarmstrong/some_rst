tests/ui/consts/promote_evaluation_unused_result.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

fn main() {

    let _: &'static usize = &(loop {}, 1).1;
}


