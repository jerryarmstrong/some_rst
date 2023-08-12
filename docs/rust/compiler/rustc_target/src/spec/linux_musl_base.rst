compiler/rustc_target/src/spec/linux_musl_base.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::crt_objects::{self, LinkSelfContainedDefault};
use crate::spec::TargetOptions;

pub fn opts() -> TargetOptions {
    let mut base = super::linux_base::opts();

    base.env = "musl".into();
    base.pre_link_objects_self_contained = crt_objects::pre_musl_self_contained();
    base.post_link_objects_self_contained = crt_objects::post_musl_self_contained();
    base.link_self_contained = LinkSelfContainedDefault::Musl;

    // These targets statically link libc by default
    base.crt_static_default = true;

    base
}


