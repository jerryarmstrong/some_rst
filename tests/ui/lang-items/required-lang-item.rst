tests/ui/lang-items/required-lang-item.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

#![feature(lang_items, no_core)]
#![no_core]

#[lang="copy"] pub trait Copy { }
#[lang="sized"] pub trait Sized { }

// error-pattern:requires `start` lang_item

fn main() {}


