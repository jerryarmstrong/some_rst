tests/ui/invalid-compile-flags/branch-protection-missing-pac-ret.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: BADFLAGS BADTARGET
// [BADFLAGS] compile-flags: --target=aarch64-unknown-linux-gnu -Zbranch-protection=leaf
// [BADFLAGS] check-fail
// [BADFLAGS] needs-llvm-components: aarch64
// [BADTARGET] compile-flags: --target=x86_64-unknown-linux-gnu -Zbranch-protection=bti
// [BADTARGET] check-fail
// [BADTARGET] needs-llvm-components: x86

#![crate_type = "lib"]
#![feature(no_core, lang_items)]
#![no_core]

#[lang="sized"]
trait Sized { }


