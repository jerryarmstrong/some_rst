src/tools/rustfmt/tests/target/configs/imports_layout/horizontal_vertical.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_indent: Block
// rustfmt-imports_layout: HorizontalVertical

use comment::{contains_comment, recover_comment_removed, rewrite_comment, FindUncommented};
use lists::{
    definitive_tactic,
    itemize_list,
    shape_for_tactic,
    struct_lit_formatting,
    struct_lit_shape,
    struct_lit_tactic,
    write_list,
    DefinitiveListTactic,
    ListFormatting,
    ListItem,
    ListTactic,
    SeparatorTactic,
};


