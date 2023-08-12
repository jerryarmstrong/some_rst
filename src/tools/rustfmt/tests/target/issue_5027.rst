src/tools/rustfmt/tests/target/issue_5027.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

pub type Iter<'a, D> = impl DoubleEndedIterator<Item = (SomethingSomethingSomethingLongType<D>)>
    + ExactSizeIterator
    + 'a;

trait FOo {
    pub type Iter<'a, D> = impl DoubleEndedIterator<Item = (SomethingSomethingSomethingLongType<D>)>
        + ExactSizeIterator
        + 'a;
}

impl Bar {
    type Iter<'a, D> = impl DoubleEndedIterator<Item = (SomethingSomethingSomethingLongType<D>)>
        + ExactSizeIterator
        + 'a;
}


