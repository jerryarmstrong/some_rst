tests/rustdoc/sort-modules-by-appearance.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests the rustdoc --sort-modules-by-appearance option, that allows module declarations to appear
// in the order they are declared in the source code, rather than only alphabetically.

// compile-flags: -Z unstable-options --sort-modules-by-appearance

pub mod module_b {}

pub mod module_c {}

pub mod module_a {}

// @matchesraw 'sort_modules_by_appearance/index.html' '(?s)module_b.*module_c.*module_a'
// @matchesraw 'sort_modules_by_appearance/sidebar-items.js' '"module_b".*"module_c".*"module_a"'


