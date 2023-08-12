tests/ui/parser/inner-attr-after-doc-comment.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(lang_items)]
/**
 * My module
 */

#![recursion_limit="100"]
//~^ ERROR an inner attribute is not permitted following an outer doc comment
fn main() {}


