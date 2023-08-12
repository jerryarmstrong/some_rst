src/tools/rustfmt/tests/source/issue-2936.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct AStruct {
    A: u32,
    B: u32,
    C: u32,
}

impl Something for AStruct {
    fn a_func() {
        match a_val {
            ContextualParseError::InvalidMediaRule(ref err) => {
                let err: &CStr = match err.kind {
                    ParseErrorKind::Custom(StyleParseErrorKind::MediaQueryExpectedFeatureName(..)) => {
                        cstr!("PEMQExpectedFeatureName")
                    },
                };
            }
        };
    }
}


