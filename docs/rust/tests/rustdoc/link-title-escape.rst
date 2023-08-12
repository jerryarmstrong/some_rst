tests/rustdoc/link-title-escape.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(rustdoc::broken_intra_doc_links)]

#![crate_name = "foo"]

//! hello [foo]
//!
//! [foo]: url 'title & <stuff> & "things"'

// @hasraw 'foo/index.html' 'title &amp; &lt;stuff&gt; &amp; &quot;things&quot;'


