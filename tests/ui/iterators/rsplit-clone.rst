tests/ui/iterators/rsplit-clone.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// RSplit<T, P> previously required T: Clone in order to be Clone

struct NotClone;

fn main() {
    let elements = [NotClone, NotClone, NotClone];
    let rsplit = elements.rsplit(|_| false);
    rsplit.clone();
}


