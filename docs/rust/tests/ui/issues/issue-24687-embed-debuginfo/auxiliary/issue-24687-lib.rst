tests/ui/issues/issue-24687-embed-debuginfo/auxiliary/issue-24687-lib.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

// This is a file that pulls in a separate file as a submodule, where
// that separate file has many multi-byte characters, to try to
// encourage the compiler to trip on them.

#[path = "issue-24687-mbcs-in-comments.rs"]
mod issue_24687_mbcs_in_comments;

pub use issue_24687_mbcs_in_comments::D;


