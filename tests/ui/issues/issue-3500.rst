tests/ui/issues/issue-3500.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    let x = &Some(1);
    match x {
        &Some(_) => (),
        &None => (),
    }
}


