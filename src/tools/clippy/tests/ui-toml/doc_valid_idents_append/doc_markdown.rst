src/tools/clippy/tests/ui-toml/doc_valid_idents_append/doc_markdown.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::doc_markdown)]

/// This is a special interface for ClipPy which doesn't require backticks
fn allowed_name() {}

/// OAuth and LaTeX are inside Clippy's default list.
fn default_name() {}

/// TestItemThingyOfCoolness might sound cool but is not on the list and should be linted.
fn unknown_name() {}

fn main() {}


