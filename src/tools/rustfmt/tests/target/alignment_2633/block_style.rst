src/tools/rustfmt/tests/target/alignment_2633/block_style.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-struct_field_align_threshold: 50

fn func() {
    Ok(ServerInformation {
        name:         unwrap_message_string(items.get(0)),
        vendor:       unwrap_message_string(items.get(1)),
        version:      unwrap_message_string(items.get(2)),
        spec_version: unwrap_message_string(items.get(3)),
    });
}


