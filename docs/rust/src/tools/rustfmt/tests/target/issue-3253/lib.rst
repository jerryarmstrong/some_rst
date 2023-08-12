src/tools/rustfmt/tests/target/issue-3253/lib.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
extern crate cfg_if;

cfg_if! {
    if #[cfg(target_family = "unix")] {
        mod foo;
        #[path = "paths/bar_foo.rs"]
        mod bar_foo;
    } else {
        mod bar;
        #[path = "paths/foo_bar.rs"]
        mod foo_bar;
    }
}


