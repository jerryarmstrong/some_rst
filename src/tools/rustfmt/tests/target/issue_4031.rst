src/tools/rustfmt/tests/target/issue_4031.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    with_woff2_glyf_table("tests/fonts/woff2/SFNT-TTF-Composite.woff2", |glyf| {
        let actual = glyf
            .records
            .iter()
            .map(|glyph| match glyph {
                GlyfRecord::Parsed(
                    found @ Glyph {
                        data: GlyphData::Composite { .. },
                        ..
                    },
                ) => Some(found),
                _ => None,
            })
            .find(|candidate| candidate.is_some())
            .unwrap()
            .unwrap();

        assert_eq!(*actual, expected)
    });
}


