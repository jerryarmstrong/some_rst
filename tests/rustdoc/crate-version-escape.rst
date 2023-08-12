tests/rustdoc/crate-version-escape.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-version=<script>alert("hi")</script> -Z unstable-options

#![crate_name = "foo"]

// @has 'foo/index.html' '//li[@class="version"]' 'Version <script>alert("hi")</script>'


