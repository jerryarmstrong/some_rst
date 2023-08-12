src/tools/rustfmt/tests/target/issue-3701/two.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

fn build_sorted_static_get_entry_names(
    mut entries: Vec<(u8, &'static str)>,
) -> (
    impl Fn(
        AlphabeticalTraversal,
        Box<dyn dirents_sink::Sink<AlphabeticalTraversal>>,
    ) -> BoxFuture<'static, Result<Box<dyn dirents_sink::Sealed>, Status>>
    + Send
    + Sync
    + 'static
) {
}


