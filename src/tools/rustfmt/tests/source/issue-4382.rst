src/tools/rustfmt/tests/source/issue-4382.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub const NAME_MAX: usize = {
    #[cfg(target_os = "linux")]   { 1024 }
    #[cfg(target_os = "freebsd")] {  255 }
};


