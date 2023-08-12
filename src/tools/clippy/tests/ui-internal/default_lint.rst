src/tools/clippy/tests/ui-internal/default_lint.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::internal)]
#![allow(clippy::missing_clippy_version_attribute)]
#![feature(rustc_private)]

#[macro_use]
extern crate rustc_middle;
#[macro_use]
extern crate rustc_session;
extern crate rustc_lint;

declare_tool_lint! {
    pub clippy::TEST_LINT,
    Warn,
    "",
    report_in_external_macro: true
}

declare_tool_lint! {
    pub clippy::TEST_LINT_DEFAULT,
    Warn,
    "default lint description",
    report_in_external_macro: true
}

declare_lint_pass!(Pass => [TEST_LINT]);
declare_lint_pass!(Pass2 => [TEST_LINT_DEFAULT]);

fn main() {}


