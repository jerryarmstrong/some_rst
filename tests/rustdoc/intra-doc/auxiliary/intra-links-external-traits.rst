tests/rustdoc/intra-doc/auxiliary/intra-links-external-traits.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait ThisTrait {
    fn asdf(&self);

    /// let's link to [`asdf`](ThisTrait::asdf)
    fn qwop(&self);
}


