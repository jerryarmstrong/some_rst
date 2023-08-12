src/tools/rustfmt/tests/source/alignment_2633/visual_style.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-struct_field_align_threshold: 50
// rustfmt-indent_style: Visual

fn func() {
    Ok(ServerInformation { name:         unwrap_message_string(items.get(0)),
           vendor: unwrap_message_string(items.get(1)),
           version: unwrap_message_string(items.get(2)),
           spec_version: unwrap_message_string(items.get(3)), });
}


