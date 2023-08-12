tests/ui/issues/issue-47703-tuple.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct WithDrop;

impl Drop for WithDrop {
    fn drop(&mut self) {}
}

fn consume(x: (&mut (), WithDrop)) -> &mut () { x.0 }

fn main() {}


