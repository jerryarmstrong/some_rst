src/tools/miri/tests/pass/zst_box.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = Box::new(());
    let y = Box::new(());
    drop(y);
    let z = Box::new(());
    drop(x);
    drop(z);
}


