src/tools/rustfmt/tests/target/issue-2673-nonmodrs-mods/lib.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(non_modrs_mods)]

// Test that submodules in non-mod.rs files work. This is just an idempotence
// test since we just want to verify that rustfmt doesn't fail.

mod foo;


