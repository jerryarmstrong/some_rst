tests/ui/conditional-compilation/cfg-empty-codemap.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that empty source_maps don't ICE (#23301)

// compile-flags: --cfg ""

// error-pattern: invalid `--cfg` argument: `""` (expected `key` or `key="value"`)

pub fn main() {
}


