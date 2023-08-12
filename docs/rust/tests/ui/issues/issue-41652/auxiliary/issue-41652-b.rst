tests/ui/issues/issue-41652/auxiliary/issue-41652-b.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Tr {
    // Note: The function needs to be declared over multiple lines to reproduce
    // the crash. DO NOT reformat.
    fn f()
        where Self: Sized;
}


