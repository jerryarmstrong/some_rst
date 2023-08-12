tests/ui/filter-block-view-items.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    // Make sure that this view item is filtered out because otherwise it would
    // trigger a compilation error
    #[cfg(not_present)] use bar as foo;
}


