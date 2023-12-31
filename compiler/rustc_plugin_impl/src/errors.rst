compiler/rustc_plugin_impl/src/errors.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Errors emitted by plugin_impl

use rustc_macros::Diagnostic;
use rustc_span::Span;

#[derive(Diagnostic)]
#[diag(plugin_impl_load_plugin_error)]
pub struct LoadPluginError {
    #[primary_span]
    pub span: Span,
    pub msg: String,
}

#[derive(Diagnostic)]
#[diag(plugin_impl_malformed_plugin_attribute, code = "E0498")]
pub struct MalformedPluginAttribute {
    #[primary_span]
    #[label]
    pub span: Span,
}


