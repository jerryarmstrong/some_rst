trashheap/state/module.rs
=========================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    #[derive(Clone, Hash, Ord, PartialOrd, Eq, PartialEq)]
enum Module {
    Ownership,
    Metadata,
    Governed,
    Creators,
    Royalty,
    Rights,
    Supply,
}

