src/tools/rustfmt/tests/mod-resolver/test-submodule-issue-5119/tests/test1.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod test1 {
#[cfg(unix)]
mod sub1;
#[cfg(not(unix))]
mod sub2;

mod sub3;
}


