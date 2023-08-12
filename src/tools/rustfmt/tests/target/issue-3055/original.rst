src/tools/rustfmt/tests/target/issue-3055/original.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: true
// rustfmt-format_code_in_doc_comments: true

/// Vestibulum elit nibh, rhoncus non, euismod sit amet, pretium eu, enim. Nunc
/// commodo ultricies dui.
///
/// Should not format with text attribute
/// ```text
///           .--------------.
///           |              v
/// Park <- Idle -> Poll -> Probe -> Download -> Install -> Reboot
///           ^      ^        '          '          '
///           '      '        '          '          '
///           '      `--------'          '          '
///           `---------------'          '          '
///           `--------------------------'          '
///           `-------------------------------------'
/// ```
///
/// Should not format with ignore attribute
/// ```text
///           .--------------.
///           |              v
/// Park <- Idle -> Poll -> Probe -> Download -> Install -> Reboot
///           ^      ^        '          '          '
///           '      '        '          '          '
///           '      `--------'          '          '
///           `---------------'          '          '
///           `--------------------------'          '
///           `-------------------------------------'
/// ```
///
/// Should format with rust attribute
/// ```rust
/// let x = 42;
/// ```
///
/// Should format with no attribute as it defaults to rust
/// ```
/// let x = 42;
/// ```
fn func() {}


