tests/ui/issues/issue-1460.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// pretty-expanded FIXME #23616

pub fn main() {
    {|i: u32| if 1 == i { }}; //~ WARN unused closure that must be used
}


