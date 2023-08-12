src/tools/rustfmt/tests/target/issue-4656/lib.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate cfg_if;

cfg_if::cfg_if! {
    if #[cfg(target_family = "unix")] {
        mod format_me_please;
    }
}


