compiler/rustc_middle/src/tests.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

// FIXME(#27438): right now the unit tests of librustc_middle don't refer to any actual
//                functions generated in librustc_data_structures (all
//                references are through generic functions), but statics are
//                referenced from time to time. Due to this bug we won't
//                actually correctly link in the statics unless we also
//                reference a function, so be sure to reference a dummy
//                function.
#[test]
fn noop() {
    rustc_data_structures::__noop_fix_for_27438();
}


