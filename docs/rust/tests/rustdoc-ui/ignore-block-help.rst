tests/rustdoc-ui/ignore-block-help.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

/// ```ignore (to-prevent-tidy-error)
/// let heart = '❤️';
/// ```
//~^^^ WARNING could not parse code block
//~| NOTE on by default
//~| NOTE character literal may only contain one codepoint
//~| HELP `ignore` code blocks require valid Rust code
pub struct X;


