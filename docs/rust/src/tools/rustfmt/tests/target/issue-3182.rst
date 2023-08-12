src/tools/rustfmt/tests/target/issue-3182.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-max_width: 79
// rustfmt-wrap_comments: true

/// ```rust
/// # #![cfg_attr(not(dox), feature(cfg_target_feature, target_feature, stdsimd)not(dox), feature(cfg_target_feature, target_feature, stdsimd))]
///
/// // Est lectus hendrerit lorem, eget dignissim orci nisl sit amet massa. Etiam volutpat lobortis eros.
/// let x = 42;
/// ```
fn func() {}


