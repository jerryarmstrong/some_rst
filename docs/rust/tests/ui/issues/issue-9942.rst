tests/ui/issues/issue-9942.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    const S: usize = 23 as usize; [0; S]; ()
}


